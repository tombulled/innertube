import attr

import typing

import useragent

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
class SuggestQueries(clients.SuggestQueriesClient):
    locale: typing.Optional[models.Locale] = None

    def __attrs_post_init__(self):
        super().__attrs_post_init__()

        headers = utils.filter \
        (
            {
                str(enums.Header.USER_AGENT):      str(infos.devices[enums.Device.WEB].product()),
                str(enums.Header.REFERER):         enums.Host.SUGGEST_QUERIES.url(),
                str(enums.Header.ACCEPT_LANGUAGE): self.locale and self.locale.accept_language(),
            }
        )

        self.session.headers.update(headers)

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
