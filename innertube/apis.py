import typing

import attr

from . import clients, config, models


@attr.s(
    auto_detect=True,
    auto_attribs=True,
)
class InnerTube(clients.InnerTubeClient):
    client: str
    locale: typing.Optional[models.Locale] = None

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.client!r})"

    def __attrs_post_init__(self) -> None:
        super().__attrs_post_init__()

        context: models.Context = self.context

        self.session.headers.update(context.headers())
        self.session.params = self.session.params.merge(context.params())
        self.session.context.update(context.context())

    @property
    def context(self) -> typing.Optional[models.Context]:
        context: models.Context
        for context in config.contexts.values():
            if context.client.name == self.client:
                return context
