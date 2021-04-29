import addict
import pydantic
import furl
import parse
import requests

import useragent
import sets

import functools
import enum
import operator
import typing
import http
import http.client

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

    @classmethod
    def parse(cls, response_context: addict.Dict):
        services = addict.Dict()

        for tracker in response_context.serviceTrackingParams:
            for param in tracker.params:
                services[tracker.service][param.key] = param.value

        request_type: typing.Optional[str] = None
        request_id:   typing.Optional[str] = None

        for key, val in services.CSI.items():
            if (result := parse.parse('Get{id}_rid', key)):
                result = addict.Dict(result.named)

                request_type = result.id
                request_id   = val

        context = utils.filter \
        (
            function     = services.CSI.yt_fn,
            browse_id    = services.GFEEDBACK.browse_id,
            context      = services.GFEEDBACK.context,
            visitor_data = response_context.visitorData,
            request = utils.filter \
            (
                type = request_type,
                id   = request_id,
            ),
            client = utils.filter \
            (
                name    = services.CSI.c,
                version = services.CSI.cver,
            ),
            flags = utils.filter \
            (
                logged_in = (value := services.GFEEDBACK.logged_in) and bool(int(value)),
            ),
        )

        return cls.parse_obj(context)

    @classmethod
    def from_response(cls, response: requests.Response):
        response_data = addict.Dict(response.json())

        if (context := response_data.responseContext):
            return cls.parse(context)

class ResponseFingerprint(BaseModel):
    endpoint:  typing.Optional[str]
    request:   typing.Optional[str]
    function:  typing.Optional[str]
    browse_id: typing.Optional[str]
    context:   typing.Optional[str]
    client:    typing.Optional[str]

    @classmethod
    def from_response(cls, response: requests.Response):
        context = ResponseContext.from_response(response)

        return cls \
        (
            endpoint  = '/'.join(furl.furl(response.url).path.segments[2:]),
            request   = context.request.type,
            function  = context.function,
            browse_id = context.browse_id,
            context   = context.context,
            client    = context.client.name,
        )

class Parser(sets.Sets[ResponseFingerprint]): pass

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
    code:    http.HTTPStatus
    status:  enums.ErrorStatus
    message: str

    def __repr__(self) -> str:
        return f'<Error [{self.code} {self.reason}]>'

    def __str__(self) -> str:
        return f'{self.code} {self.reason}' + \
        (
            f': {self.message}'
            if self.message
            else ''
        )

    @property
    def reason(self):
        return http.client.responses[self.code]

class Adaptor(BaseModel):
    base_url: str
    params:   dict
    headers:  dict
    context:  dict

class Host(BaseModel):
    scheme:  str = enums.Scheme.HTTPS
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

class Schema(BaseModel):
    client:  enums.Client
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
                str(enums.YouTubeHeader.CLIENT_NAME):    str(self.service.id),
                str(enums.YouTubeHeader.CLIENT_VERSION): self.client.version,
                str(enums.Header.USER_AGENT):            str(self.user_agent()),
                str(enums.Header.REFERER):               str(self.service.host()),
                str(enums.Header.ACCEPT_LANGUAGE):       locale and locale.accept_language(),
            }
        )

    def adaptor(self, locale: Locale = None) -> Adaptor:
        return Adaptor \
        (
            base_url = self.base_url(),
            params   = self.params(),
            context  = self.client.context(locale = locale),
            headers  = self.headers(locale = locale),
        )
