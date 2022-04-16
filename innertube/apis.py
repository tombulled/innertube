import attr

import typing

from . import clients
from . import models
from . import enums
from . import infos


@attr.s(
    auto_detect=True,
    auto_attribs=True,
)
class InnerTube(clients.InnerTubeClient):
    client: enums.Client
    locale: typing.Optional[models.Locale] = None

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.schema.client})"

    def __attrs_post_init__(self) -> None:
        super().__attrs_post_init__()

        adaptor: models.Adaptor = self.info.adaptor(
            locale=self.locale,
        )

        self.session.headers.update(adaptor.headers)
        self.session.params = self.session.params.merge(adaptor.params)
        self.session.context.update(adaptor.context)

    @property
    def schema(self) -> typing.Optional[models.ClientSchema]:
        schema: models.ClientSchema
        for schema in infos.schemas:
            if schema.client == self.client:
                return schema

    @property
    def info(self) -> models.Client:
        return infos.clients[self.client]
