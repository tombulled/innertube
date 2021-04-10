import addict
import babel

import typing

from . import infos
from . import enums
from . import models
from . import clients
from . import sessions

def app \
        (
            service: enums.Service,
            device:  enums.Service,
        ) -> typing.Optional[models.App]:
    app_type:   enums.App
    app_schema: models.AppSchema

    for app_type, app_schema in infos.schemas.items():
        if app_schema.service == service and app_schema.device == device:
            return infos.apps[app_type]

def adaptor \
        (
            service: enums.Service,
            device:  enums.Service,
            locale:  typing.Optional[babel.Locale] = None,
        ) -> typing.Optional[models.Adaptor]:
    app_obj = app \
    (
        service = service,
        device  = device,
    )

    return app_obj and app_obj.adaptor \
    (
        locale = locale,
    )

def session \
        (
            service: enums.Service,
            device:  enums.Service,
            locale:  typing.Optional[babel.Locale] = None,
        ) -> typing.Optional[sessions.Session]:
    adaptor_obj = adaptor \
    (
        service = service,
        device  = device,
        locale  = locale,
    )

    data: addict.Dict = addict.Dict \
    (
        adaptor_obj.dict \
        (
            by_alias     = True,
            exclude_none = True,
        ),
    )

    session: sessions.Session = sessions.Session \
    (
        base_url = data.base_url,
        context  = data.context,
    )

    session.headers.update(data.headers)
    session.params.update(data.params)

    return session

def client \
        (
            service: enums.Service,
            device:  enums.Service,
            locale:  typing.Optional[babel.Locale] = None,
        ) -> typing.Optional[clients.Client]:
    session_obj = session \
    (
        service = service,
        device  = device,
        locale  = locale,
    )

    return session_obj and clients.Client(session_obj)
