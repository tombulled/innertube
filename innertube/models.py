'''
Library containing info models

Usage:
    >>> from innertube import models
    >>>
    >>> dir(models)
    ...
    >>>
    >>> models.DeviceInfo
    <class 'innertube.models.DeviceInfo'>
    >>>
'''

import pydantic
import humps
import furl

from . import enums
from . import utils

from typing import \
(
    Optional,
    List,
)

from babel import \
(
    Locale,
)

from .enums import \
(
    DeviceType,
    ServiceType,
    ClientType,
    AppType,
    Alt,
)

class BaseModel(pydantic.BaseModel):
    class Config:
        allow_mutation                 = False
        allow_population_by_field_name = True

    def dict(self, **kwargs):
        return utils.filter_kwargs \
        (
            ** super().dict \
            (
                ** \
                {
                    ** dict \
                    (
                        by_alias = True,
                    ),
                    ** kwargs,
                },
            ),
        )

class Params(BaseModel):
    key: str
    alt: str

class Context(BaseModel):
    client_name:    str
    client_version: str
    gl:             Optional[str]
    hl:             Optional[str]

    class Config:
        alias_generator = humps.camelize

class Headers(BaseModel):
    client_name:    str = pydantic.Field(..., alias = enums.Header.CLIENT_NAME.value)
    client_version: str = pydantic.Field(..., alias = enums.Header.CLIENT_VERSION.value)
    user_agent:     str = pydantic.Field(..., alias = enums.Header.USER_AGENT.value)
    referer:        str = pydantic.Field(..., alias = enums.Header.REFERER.value)

    class Config:
        alias_generator = lambda field: '-'.join(map(str.title, field.split('_')))

class Error(BaseModel):
    class Error(BaseModel):
        reason: str
        domain: str
        message: str

    code: int
    status: str
    message: str
    errors: Optional[List[Error]]

class AdaptorInfo(BaseModel):
    base_url: str
    params:   Params
    headers:  Headers
    context:  Context

class ProductInfo(BaseModel):
    name:    str = 'Mozilla'
    version: str = '5.0'
    token:   str

    def user_agent(self) -> str:
        return f'{self.name}/{self.version} ({self.token})'

class DeviceInfo(BaseModel):
    '''
    Info Model for storing information about a Device
    '''

    type:    DeviceType
    name:    str
    token:   str
    package: Optional[str]

class ServiceInfo(BaseModel):
    '''
    Info Model for storing information about a Service
    '''

    type:      ServiceType
    name:      str
    domain:    str
    id:        int

class ApiInfo(BaseModel):
    '''
    Info Model for storing information about an Api
    '''

    key:     str
    domain:  str = 'youtubei.googleapis.com'
    mount:   str = 'youtubei'
    version: int = 1

class ClientInfo(BaseModel):
    '''
    Info Model for storing information about a Client
    '''

    type:       ClientType
    name:       str
    version:    str
    identifier: Optional[str]

class AppInfo(BaseModel):
    type:    AppType
    client:  ClientInfo
    device:  DeviceInfo
    service: ServiceInfo
    api:     ApiInfo
    project: Optional[str]

    def product(self) -> ProductInfo:
        return ProductInfo \
        (
            ** utils.filter_kwargs \
            (
                name    = self.package(),
                version = self.project and self.client.version,
                token   = self.device.token,
            ),
        )

    def package(self) -> Optional[str]:
        if self.device.package and self.project:
            return f'{self.device.package}.{self.project}'

    def base_url(self) -> str:
        return str \
        (
            furl.furl \
            (
                scheme = enums.Scheme.HTTPS.value,
                host   = self.api.domain,
                path   = furl.Path() / self.api.mount / f'v{self.api.version}' / '/',
            )
        )

    def params(self) -> Params:
        return Params \
        (
            key = self.api.key,
            alt = enums.Alt.JSON.value,
        )

    def context(self, locale: Locale = None) -> Context:
        return Context \
        (
            client_name    = self.client.name,
            client_version = self.client.version,
            gl = locale and (locale.territory or locale.language),
            hl = locale and '-'.join \
            (
                utils.filter_args \
                (
                    locale.language,
                    locale.territory,
                ),
            ),
        )

    def headers(self) -> Headers:
        return Headers \
        (
            client_name    = str(self.service.id),
            client_version = self.client.version,
            user_agent     = self.product().user_agent(),
            referer        = str \
            (
                furl.furl \
                (
                    scheme = enums.Scheme.HTTPS.value,
                    host   = self.service.domain,
                ),
            ),
        )

    def adaptor_info(self, locale: Locale = None) -> AdaptorInfo:
        return AdaptorInfo \
        (
            base_url = self.base_url(),
            params   = self.params(),
            context  = self.context(locale = locale),
            headers  = self.headers(),
        )
