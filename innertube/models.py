import pydantic
import babel
import furl

import functools
import enum
import operator
import typing

from . import enums
from . import utils

class BaseModel(pydantic.BaseModel): pass

class Locale(BaseModel):
    hl: str
    gl: typing.Optional[str]

    def accept(self):
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

class SubError(BaseModel):
    reason:  str
    domain:  str
    message: str

class Error(BaseModel):
    code:    int
    status:  str
    message: str
    errors:  typing.Optional[typing.List[SubError]]

class Adaptor(BaseModel):
    base_url: str
    params:   dict
    headers:  dict
    context:  dict

class ProductIdentifier(BaseModel):
    name:     str
    version:  typing.Optional[str]

    def __str__(self):
        return '/'.join \
        (
            filter \
            (
                lambda item: item is not None,
                (
                    self.name,
                    self.version,
                ),
            ),
        )

class ProductComment(BaseModel):
    comments: typing.List[str]

    def __str__(self):
        return '({comments})'.format \
        (
            comments = '; '.join \
            (
                self.comments,
            ),
        )

class Product(BaseModel):
    identifier: ProductIdentifier
    comment:    typing.Optional[ProductComment]

    def __str__(self):
        return ' '.join \
        (
            map \
            (
                str,
                filter \
                (
                    lambda item: item is not None,
                    (
                        self.identifier,
                        self.comment,
                    ),
                ),
            ),
        )

class UserAgent(BaseModel):
    products: typing.List[Product]

    def __str__(self):
        return ' '.join(map(str, self.products))

class Company(BaseModel):
    name:   str
    domain: str

    def package(self):
        return '.'.join(self.domain.split('.')[::-1])

class Device(BaseModel):
    class Product(BaseModel):
        identifier: typing.Optional[ProductIdentifier]
        comment:    typing.Optional[ProductComment]

        def product(self) -> typing.Optional[Product]:
            return self.identifier and Product \
            (
                identifier = self.identifier,
                comment    = self.comment,
            )

    name:       str
    identifier: str
    product:    Product

    def user_agent(self) -> typing.Optional[UserAgent]:
        return (product := self.product.product()) and UserAgent \
        (
            products = [product],
        )

class Host(BaseModel):
    scheme:  str = enums.Scheme.HTTPS.value
    domain:  str
    port:    typing.Optional[int]

    def __str__(self):
        return str \
        (
            furl.furl \
            (
                scheme = self.scheme,
                host   = self.domain,
                port   = self.port,
                path   = '/',
            )
        )

class Api(BaseModel):
    host:    Host
    company: Company
    mount:   typing.Optional[str]
    version: typing.Optional[str]

    def __str__(self):
        return str \
        (
            furl.furl \
            (
                url  = str(self.host),
                path = furl.Path(self.mount) / '/',
            ),
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

    def api(self) -> Api:
        return Api \
        (
            host = self.host(),
        )

class Authentication(BaseModel):
    api_key: str

class Client(BaseModel):
    name:       str
    version:    str
    auth:       Authentication
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

class Consumer(BaseModel):
    device:  Device
    api:     Api

    def headers(self, locale: Locale = None) -> dict:
        return utils.filter \
        (
            ** \
            {
                enums.Header.USER_AGENT.value:      str(self.device.user_agent()),
                enums.Header.REFERER.value:         str(self.api),
                enums.Header.ACCEPT_LANGUAGE.value: locale and locale.accept(),
            }
        )

class Application(BaseModel):
    client:   Client
    service:  Service
    consumer: Consumer

    def product(self) -> Product:
        return self.consumer.device.product.product() or Product \
        (
            identifier = ProductIdentifier \
            (
                name    = self.package(),
                version = self.client.version,
            ),
            comment    = self.consumer.device.product.comment,
        )

    def user_agent(self) -> UserAgent:
        return UserAgent \
        (
            products = [self.product()],
        )

    def base_url(self) -> str:
        return str(self.consumer.api)

    def package(self) -> str:
        segments = \
        (
            self.consumer.api.company.package(),
            self.consumer.device.identifier,
            self.client.package,
        )

        if all(segments):
            return '.'.join(segments)

    def params(self) -> dict:
        return dict \
        (
            key = self.client.auth.api_key,
            alt = enums.Alt.JSON.value,
        )

    def headers(self, locale: Locale = None) -> dict:
        return utils.filter \
        (
            ** \
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
