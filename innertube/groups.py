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
    service: enums.Service                  = attr.ib()
    locale:  typing.Optional[babel.Locale]  = attr.ib()

    def __init__ \
            (
                self,
                service: enums.Service,
                devices: typing.List[enums.Device],
                locale:  typing.Optional[models.Locale] = None,
            ):
        super().__init__ \
        (
            clients = \
            {
                device: constructors.client \
                (
                    service = service,
                    device  = device,
                    locale  = locale,
                )
                for device in devices
            }
        )

        self.service = service
        self.locale  = locale
