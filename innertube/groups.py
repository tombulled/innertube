import attr

import typing

from . import enums
from . import clients
from . import constructors
from . import models

@attr.s
class BaseClientGroup(object):
    clients = attr.ib()

    def __call__(self, device: enums.Device):
        return self.clients.get(device)

@attr.s(init = False)
class ClientGroup(BaseClientGroup):
    service: enums.Service = attr.ib()

    def __init__ \
            (
                self,
                service: enums.Service,
                devices: typing.List[enums.Device],
            ):
        super().__init__ \
        (
            clients = \
            {
                device: constructors.client \
                (
                    service = service,
                    device  = device,
                )
                for device in devices
            }
        )

        self.service = service
