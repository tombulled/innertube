import typing

from . import clients
from . import enums
from . import models
from . import infos

class SuggestQueries(clients.SuggestQueriesClient):
    def __init__(self, locale: typing.Optional[models.Locale] = None):
        super().__init__()

        # TODO (as Consumer model removed)
        # device = infos.devices[enums.Device.WEB]
        #
        # consumer = models.Consumer \
        # (
        #     host   = infos.hosts[enums.Host.SUGGEST_QUERIES],
        #     device = infos.devices[enums.Device.WEB],
        # )
        #
        # self.adaptor.session.headers.update(consumer.headers(locale = locale))

class InnerTube(clients.InnerTubeClient):
    def __init__(self, client: enums.Client, locale: typing.Optional[models.Locale] = None):
        super().__init__()

        schema = infos.schemas[client]

        app = models.Application \
        (
            client  = infos.clients[client],
            service = infos.services[schema.service],
            device  = infos.devices[schema.device],
            api     = infos.hosts[enums.Host.YOUTUBEI],
            company = infos.companies[enums.Company.GOOGLE],
        )

        adaptor = app.adaptor \
        (
            locale = locale,
        )

        self.adaptor.headers.update(adaptor.headers)
        self.adaptor.params.update(adaptor.params)
        self.adaptor.context.update(adaptor.context)
