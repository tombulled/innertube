import attr
import toolz

import typing

from . import clients
from . import enums
from . import models
from . import infos

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

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

@attrs
class InnerTube(clients.InnerTubeClient):
    client: enums.Client
    locale: typing.Optional[models.Locale] = None

    def __attrs_post_init__(self):
        adaptor = self.info.adaptor \
        (
            locale = self.locale,
        )

        self.adaptor.session.headers.update(adaptor.headers)
        self.adaptor.session.params.update(adaptor.params)
        self.adaptor.session.context.update(adaptor.context)

    @property
    def schema(self) -> models.Schema:
        return next \
        (
            filter \
            (
                lambda schema: schema.client == self.client,
                infos.schemas,
            ),
        )

    @property
    def info(self) -> models.Client:
        schema = self.schema

        return models.Application \
        (
            client  = infos.clients[self.client],
            service = infos.services[self.schema.service],
            device  = infos.devices[self.schema.device],
            api     = infos.hosts[enums.Host.YOUTUBEI],
            company = infos.companies[enums.Company.GOOGLE],
        )

    @property
    def device(self) -> models.Device:
        return infos.devices[self.schema.device]

    @property
    def service(self) -> models.Service:
        return infos.services[self.schema.service]
