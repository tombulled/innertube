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

from . import constants

from typing import \
(
    Optional,
    List,
)

from .enums import \
(
    ApiEndpoint,
)

class BaseModel(pydantic.BaseModel): pass

class DeviceInfo(BaseModel):
    '''
    Info Model for storing information about a Device
    '''

    name:          str
    product_token: str
    package:       Optional[str]

class ServiceInfo(BaseModel):
    '''
    Info Model for storing information about a Service
    '''

    name:      str
    domain:    str
    id:        int
    endpoints: List[ApiEndpoint]

class ApiInfo(BaseModel):
    '''
    Info Model for storing information about an Api
    '''

    key:     str
    domain:  str = 'youtubei.googleapis.com'
    version: int = 1

class ClientInfo(BaseModel):
    '''
    Info Model for storing information about a Client
    '''

    name:       str
    version:    str
    identifier: Optional[str]

class AppInfo(BaseModel):
    client:  ClientInfo
    device:  DeviceInfo
    service: ServiceInfo
    api:     ApiInfo
    project: Optional[str]

    @property
    def user_agent(self) -> str:
        return '{product_name}/{product_version} {product_token}'.format \
        (
            product_name    = self.package or constants.DEFAULT_PRODUCT_NAME,
            product_version = self.package and self.client.version or constants.DEFAULT_PRODUCT_VERSION,
            product_token   = self.device.product_token,
        )

    @property
    def package(self) -> Optional[str]:
        if self.device.package and self.project:
            return f'{self.device.package}.{self.project}'
