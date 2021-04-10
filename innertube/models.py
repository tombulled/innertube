import pydantic
import humps
import babel
import furl

import functools
import enum
import operator
import typing

from . import enums

class BaseModel(pydantic.BaseModel):
    class Config:
        allow_population_by_field_name = True

class Params(BaseModel):
    key: str
    alt: enums.Alt

class Context(BaseModel):
    client_name:    typing.Optional[str]
    client_version: typing.Optional[str]
    gl:             typing.Optional[str]
    hl:             typing.Optional[str]

    class Config:
        alias_generator = humps.camelize

class Headers(BaseModel):
    client_name:    typing.Optional[str] = pydantic.Field(..., alias = enums.Header.CLIENT_NAME.value)
    client_version: typing.Optional[str] = pydantic.Field(..., alias = enums.Header.CLIENT_VERSION.value)
    user_agent:     typing.Optional[str] = pydantic.Field(..., alias = enums.Header.USER_AGENT.value)
    referer:        typing.Optional[str] = pydantic.Field(..., alias = enums.Header.REFERER.value)

    class Config:
        alias_generator = lambda field: '-'.join(map(str.title, field.split('_')))

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
    params:   Params
    headers:  Headers
    context:  Context

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

        def product(self):
            return self.identifier and Product \
            (
                identifier = self.identifier,
                comment    = self.comment,
            )

    name:    str
    product: Product
    project: typing.Optional[str]

class Service(BaseModel):
    name:   str
    domain: str
    id:     typing.Optional[int]

class Host(BaseModel):
    scheme:  enums.Scheme = enums.Scheme.HTTPS
    domain:  str
    port:    typing.Optional[int]

    def __str__(self):
        return str \
        (
            furl.furl \
            (
                scheme = self.scheme.value,
                host   = self.domain,
                port   = self.port,
            )
        )

class Api(BaseModel):
    host:    Host
    mount:   typing.Optional[str]
    version: typing.Optional[str]

    def __str__(self):
        return str \
        (
            functools.reduce \
            (
                operator.truediv,
                (
                    map \
                    (
                        lambda item: item or '',
                        (
                            furl.furl(str(self.host)),
                            self.mount,
                            self.version,
                        )
                    )
                )
            )
        )

class Authentication(BaseModel):
    api_key: str

class Client(BaseModel):
    name:       str
    version:    str
    auth:       Authentication
    module:     typing.Optional[str]
    identifier: typing.Optional[str]

    def product(self):
        return ProductIdentifier \
        (
            name    = self.name,
            version = self.version,
        )

class AppSchema(BaseModel):
    client:  enums.Client
    device:  enums.Device
    service: enums.Service

class App(BaseModel):
    company: Company
    client:  Client
    device:  Device
    service: Service
    api:     Api

    def product(self) -> Product:
        return self.device.product.product() or Product \
        (
            identifier = self.client.product(),
            comment    = self.device.product.comment,
        )

    def user_agent(self) -> UserAgent:
        return UserAgent \
        (
            products = [self.product()],
        )

    def base_url(self) -> str:
        return str(self.api)

    def package(self) -> str:
        segments = \
        (
            self.company.package(),
            self.device.project,
            self.module,
        )

        if all(segments):
            return '.'.join(segments)

    def params(self) -> Params:
        return Params \
        (
            key = self.client.auth.api_key,
            alt = enums.Alt.JSON,
        )

    def context(self, locale: babel.Locale = None) -> Context:
        return Context \
        (
            client_name    = self.client.name,
            client_version = self.client.version,
            gl = locale and (locale.territory or locale.language),
            hl = locale and '-'.join \
            (
                filter \
                (
                    lambda item: item is not None,
                    (
                        locale.language,
                        locale.territory,
                    ),
                ),
            ),
        )

    def headers(self) -> Headers:
        return Headers \
        (
            client_name    = self.service.id,
            client_version = self.client.version,
            user_agent     = str(self.user_agent()),
            referer        = str \
            (
                furl.furl \
                (
                    scheme = enums.Scheme.HTTPS.value,
                    host   = self.service.domain,
                ),
            ),
        )

    def adaptor(self, locale: babel.Locale = None) -> Adaptor:
        return Adaptor \
        (
            base_url = self.base_url(),
            params   = self.params(),
            context  = self.context(locale = locale),
            headers  = self.headers(),
        )
