import attr
import babel

import typing

from . import clients
from . import enums

from .clients import \
(
    Client,
)

@attr.s
class BaseClientGroup(object):
    clients: typing.Dict[enums.DeviceType, Client] = attr.ib \
    (
        repr = lambda clients: tuple \
        (
            client.info.name
            for client in clients.values()
        ).__str__()
    )

    def __call__(self, device: enums.DeviceType) -> Client:
        return self.clients.get(device)

    def __repr__(self) -> str:
        return repr \
        (
            pydantic.create_model \
            (
                self.__class__.__name__,
                clients = \
                [
                    client.info.name
                    for client in self.clients.values()
                ],
            )()
        )

class ClientGroup(BaseClientGroup):
    __service: enums.ServiceType
    __locale:  typing.Optional[babel.Locale]

    def __init__ \
            (
                self,
                service:  enums.ServiceType,
                *devices: enums.DeviceType,
                locale:   babel.Locale = None,
            ):
        super().__init__ \
        (
            clients = \
            {
                device: clients.Client.construct \
                (
                    service = service,
                    device  = device,
                    locale  = locale,
                )
                for device in devices
            }
        )

        self.__service = service
        self.__locale  = locale

    @property
    def service(self) -> enums.ServiceType:
        return self.__service

    @property
    def locale(self) -> typing.Optional[babel.Locale]:
        return self.__locale
