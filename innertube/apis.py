import attr

import typing

from . import clients
from . import models
from . import enums
from . import infos
from . import utils

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class InnerTube(clients.InnerTubeClient):
    client: enums.Client
    locale: typing.Optional[models.Locale] = None

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.schema.client})'

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
    def schema(self) -> models.ClientSchema:
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
        return infos.clients[self.client]
