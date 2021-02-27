import pydantic
from typing import Union
from . import types

class DeviceInfo(pydantic.BaseModel):
    name: str
    type: types.DeviceType

class ServiceInfo(pydantic.BaseModel):
    name:     str
    type:     types.ServiceType
    domain:   str
    id:       int

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

    @property
    def user_agent(self):
        builders = \
        {
            types.DeviceType.Web:     lambda info: 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
            types.DeviceType.Android: lambda info: f'{info.package}/{info.version}(Linux; U; Android 9; en_GB; VirtualBox Build/PI)',
            types.DeviceType.Ios:     lambda info: f'{info.package}/{info.version} (iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB)',
            types.DeviceType.Tv:      lambda info: 'Mozilla/5.0 (PlayStation; PlayStation 4/8.03) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.0 Safari/605.1.15',
        }

        if self.device.type in builders:
            return builders[self.device.type](self)

        return buillders[types.DeviceType.Web]()
