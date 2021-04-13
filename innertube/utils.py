import typing

from . import enums
from . import infos

def client(service: enums.Service, device: enums.Device) -> typing.Optional[enums.Client]:
    for client, schema in infos.schemas.items():
        if schema.service == service and schema.device == device:
            return client
