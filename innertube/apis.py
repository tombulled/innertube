import attr

import typing

from . import clients
from . import models
from . import enums
from . import infos

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class SuggestQueries(clients.SuggestQueriesClient):
    locale: typing.Optional[models.Locale] = None

    def __attrs_post_init__(self):
        # TODO: initialise...
        pass

@attrs
class InnerTube(clients.InnerTubeClient):
    client: enums.Client
    locale: typing.Optional[models.Locale] = None

    def __attrs_post_init__(self):
        super().__attrs_post_init__()
        
        adaptor = self.info.adaptor \
        (
            locale = self.locale,
        )

        self.session.headers.update(adaptor.headers)
        self.session.params.update(adaptor.params)
        self.session.context.update(adaptor.context)

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
