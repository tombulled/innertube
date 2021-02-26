import innertube
from pprint import pprint as pp

from innertube import utils, types

from typing import Union

from innertube import maps, info

def get_client(*, service: Union[info.ServiceInfo, types.ServiceType], device: Union[info.DeviceInfo, types.DeviceType]):
    service_type = service if isinstance(service, types.ServiceType) else service.type
    device_type  = device  if isinstance(device, types.DeviceType)   else device.type

    # for

c = get_client \
(
    service = innertube.services.YouTubeMusic,
    device  = innertube.devices.Android,
)
