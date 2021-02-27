import pydantic

from . import types
from typing import Union

class DeviceInfo(pydantic.BaseModel):
    name: str
    type: types.DeviceType

class ServiceInfo(pydantic.BaseModel):
    name:     str
    type:     types.ServiceType
    domain:   str

class ApiInfo(pydantic.BaseModel):
    key:     str
    domain:  str = 'youtubei.googleapis.com'
    version: int = 1

class ClientInfo(pydantic.BaseModel):
    name:    str
    version: str

    device:  DeviceInfo
    service: ServiceInfo
    api:     ApiInfo

    package: Union[None, str]
