import typing

from . import enums
from . import models
from . import infos
from . import sessions
from . import clients

def suggest_queries \
        (
            device: enums.Device  = enums.Device.WEB,
            locale: models.Locale = None,
        ):
    api    = infos.apis[enums.Api.SUGGEST_QUERIES]
    device = infos.devices[device]

    consumer = models.Consumer \
    (
        api    = infos.apis[enums.Api.SUGGEST_QUERIES],
        device = infos.devices[enums.Device.WEB],
    )

    session = sessions.BaseUrlSession \
    (
        base_url = str(api),
    )

    session.headers.update(consumer.headers(locale = locale))

    return clients.SuggestQueries \
    (
        session = session,
    )

def innertube \
        (
            service: enums.Service,
            device:  enums.Device                   = enums.Device.WEB,
            locale:  typing.Optional[models.Locale] = None,
        ) -> typing.Optional[clients.InnerTube]:
    for client, schema in infos.schemas.items():
        if schema.service == service and schema.device == device:
            break
    else:
        return

    app = models.Application \
    (
        client   = infos.clients[client],
        service  = infos.services[service],
        consumer = models.Consumer \
        (
            api    = infos.apis[enums.Api.YOUTUBEI_V1],
            device = infos.devices[device],
        ),
    )

    adaptor = app.adaptor \
    (
        locale = locale,
    )

    session: sessions.Session = sessions.Session \
    (
        base_url = adaptor.base_url,
        context  = adaptor.context,
    )

    session.headers.update(adaptor.headers)
    session.params.update(adaptor.params)

    return clients.InnerTube \
    (
        session = session,
    )
