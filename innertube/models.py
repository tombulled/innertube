import pydantic
import babel
import furl

import useragent
import sets

import functools
import enum
import operator
import typing

from . import enums
from . import utils

class BaseModel(pydantic.BaseModel): pass

class ResponseContext(BaseModel):
    class Request(BaseModel):
        type: typing.Optional[str]
        id:   typing.Optional[str]

    class Client(BaseModel):
        name:    typing.Optional[str]
        version: typing.Optional[str]

    class Flags(BaseModel):
        logged_in: typing.Optional[bool]

    function:     typing.Optional[str]
    browse_id:    typing.Optional[str]
    context:      typing.Optional[str]
    visitor_data: typing.Optional[str]
    client:       typing.Optional[Client]  = pydantic.Field(default_factory = Client)
    request:      typing.Optional[Request] = pydantic.Field(default_factory = Request)
    flags:        typing.Optional[Flags]   = pydantic.Field(default_factory = Flags)

class ResponseFingerprint(BaseModel):
    endpoint:  typing.Optional[str]
    request:   typing.Optional[str]
    function:  typing.Optional[str]
    browse_id: typing.Optional[str]
    context:   typing.Optional[str]
    client:    typing.Optional[str]

class Parser(sets.Sets[ResponseFingerprint]): pass

# class Parser(BaseModel):
#     request:   typing.Optional[typing.Set[str]] = pydantic.Field(default_factory = set)
#     function:  typing.Optional[typing.Set[str]] = pydantic.Field(default_factory = set)
#     browse_id: typing.Optional[typing.Set[str]] = pydantic.Field(default_factory = set)
#     context:   typing.Optional[typing.Set[str]] = pydantic.Field(default_factory = set)
#     client:    typing.Optional[typing.Set[str]] = pydantic.Field(default_factory = set)

class Locale(BaseModel):
    hl: str
    gl: typing.Optional[str]

    def accept_language(self):
        return ','.join \
        (
            filter \
            (
                lambda item: item is not None,
                (
                    self.hl,
                    self.gl,
                )
            )
        )

class Error(BaseModel):
    class Error(BaseModel):
        reason:  str
        domain:  str
        message: str

        def __str__(self) -> str:
            return f'{self.reason}@{self.domain}: {self.message}'

    code:    int
    status:  str
    message: str
    errors:  typing.Optional[typing.List[Error]]

    def __str__(self) -> str:
        return '\n\t'.join \
        (
            (
                f'[{self.code}] {self.status}: {self.message}',
                * \
                (
                    str(error)
                    for error in self.errors or ()
                )
            )
        )

class Adaptor(BaseModel):
    base_url: str
    params:   dict
    headers:  dict
    context:  dict

class Host(BaseModel):
    scheme:  str = enums.Scheme.HTTPS.value
    domain:  str
    port:    typing.Optional[int]
    path:    str = '/'

    def __str__(self):
        return str \
        (
            furl.furl \
            (
                scheme = self.scheme,
                host   = self.domain,
                port   = self.port,
                path   = self.path,
            )
        )

    def __truediv__(self, rhs):
        return self.copy \
        (
            update = dict \
            (
                path = str(furl.Path(self.path) / rhs),
            ),
        )

class Company(BaseModel):
    name:   str
    domain: str

    def package(self):
        return '.'.join(self.domain.split('.')[::-1])

    def host(self):
        return Host \
        (
            domain = self.domain,
        )

class Device(BaseModel):
    name:       str
    identifier: str
    comments:   typing.List[str]
    product:    typing.Optional[useragent.ProductIdentifier]

    def user_agent(self) -> typing.Optional[useragent.UserAgent]:
        return (identifier := self.product) and useragent.UserAgent \
        (
            products = \
            [
                useragent.Product \
                (
                    identifier = identifier,
                    comments   = self.comments,
                )
            ],
        )

class Service(BaseModel):
    name:       str
    identifier: str
    domain:     str
    id:         typing.Optional[int]

    def host(self) -> Host:
        return Host \
        (
            domain = self.domain,
        )

class Client(BaseModel):
    name:       str
    version:    str
    key:        str
    package:    typing.Optional[str]
    identifier: typing.Optional[str]

    def context(self, locale: Locale = None) -> dict:
        return dict \
        (
            clientName    = self.name,
            clientVersion = self.version,
            ** (locale.dict() if locale else {}),
        )

class ClientSchema(BaseModel):
    device:  enums.Device
    service: enums.Service

class Application(BaseModel):
    client:   Client
    service:  Service
    device:   Device
    api:      Host
    company:  Company

    def base_url(self) -> str:
        return str(self.api)

    def package(self) -> typing.Optional[str]:
        segments = \
        (
            self.company.package(),
            self.device.identifier,
            self.client.package,
        )

        if all(segments):
            return '.'.join(segments)

    def params(self) -> dict:
        return dict \
        (
            key = self.client.key,
            alt = enums.Alt.JSON.value,
        )

    def product(self) -> useragent.Product:
        if (identifier := self.device.product):
            return useragent.Product \
            (
                identifier = identifier,
                comments   = self.device.comments,
            )
        else:
            return useragent.Product \
            (
                identifier = useragent.ProductIdentifier \
                (
                    name    = self.package(),
                    version = self.client.version,
                ),
                comments = self.device.comments,
            )

    def user_agent(self) -> useragent.UserAgent:
        return useragent.UserAgent \
        (
            products = \
            [
                self.product(),
            ],
        )

    def headers(self, locale: Locale = None) -> dict:
        return utils.filter \
        (
            {
                enums.YouTubeHeader.CLIENT_NAME.value:    str(self.service.id),
                enums.YouTubeHeader.CLIENT_VERSION.value: self.client.version,
                enums.Header.USER_AGENT.value:            str(self.user_agent()),
                enums.Header.REFERER.value:               str(self.service.host()),
                enums.Header.ACCEPT_LANGUAGE.value:       locale and locale.accept(),
            }
        )

    def adaptor(self, locale: babel.Locale = None) -> Adaptor:
        return Adaptor \
        (
            base_url = self.base_url(),
            params   = self.params(),
            context  = self.client.context(locale = locale),
            headers  = self.headers(locale = locale),
        )
