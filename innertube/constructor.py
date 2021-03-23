import babel

import typing

from . import client
from . import session
from . import enums
from . import infos

def construct_client \
        (
            service: enums.ServiceType,
            device:  enums.DeviceType,
            locale:  babel.Locale = None,
        ) -> typing.Optional[client.Client]:
    app_info = infos.Apps.get \
    (
        service = infos.Services.get(type = service),
        device  = infos.Devices.get(type = device),
    )

    if app_info:
        return client.Client \
        (
            session = session.Session \
            (
                info = app_info.adaptor_info \
                (
                    locale = locale,
                ),
            )
        )
