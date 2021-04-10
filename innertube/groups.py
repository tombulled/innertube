import attr
import babel

import typing

from . import enums
from . import clients
from . import constructors

@attr.s
class BaseClientGroup(object):
    clients = attr.ib()

    def __call__(self, device: enums.Device):
        return self.clients.get(device)

@attr.s(init = False)
class ClientGroup(BaseClientGroup):
    service: enums.Service                  = attr.ib()
    locale:  typing.Optional[babel.Locale]  = attr.ib()

    def __init__ \
            (
                self,
                service: enums.Service,
                devices: enums.Device,
                locale:  typing.Optional[babel.Locale] = None,
            ):
        super().__init__ \
        (
            clients = \
            [
                constructors.client \
                (
                    service = service,
                    device  = device,
                    locale  = locale,
                )
                for device in devices
            ]
        )

        self.service = service
        self.locale  = locale
