import attr
import requests

import re
import typing
import operator
import functools

import register

from . import enums
from . import models
from . import types
from . import parsers
from . import infos
from . import sessions

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class BaseClient(object):
    session: requests.Session

@attrs
class BaseInnerTube(BaseClient):
    parsers: register.HookedRegister = attr.ib \
    (
        default = attr.Factory \
        (
            functools.partial \
            (
                register.HookedRegister,
                models.Parser,
            )
        ),
        repr = False,
    )

    def __attrs_post_init__(self):
        self.parsers()(lambda data: data)

    def __call__(self, *args, **kwargs) -> types.Dict:
        response = types.Dict(self.session.post(*args, **kwargs).json())

        response_context: models.ResponseContext = parsers.response_context(response.responseContext)

        for parser, schema in reversed(self.parsers.items()):
            value_map = \
            {
                response_context.client.name:  schema.client,
                response_context.request.type: schema.request,
                response_context.browse_id:    schema.browse_id,
                response_context.function:     schema.function,
                response_context.context:      schema.context,
            }

            parser_match = all \
            (
                value is None \
                    or values is None
                    or value  in values
                for value, values in value_map.items()
            )

            if parser_match:
                return parser(response)

        # TODO: Raise appropriate exception
        raise Exception(f'No parser found for context: {response_context!s}')

    def config(self) -> types.Dict:
        return self('config')

    def guide(self) -> types.Dict:
        return self('guide')

    def player(self, *, video_id: str) -> types.Dict:
        return self \
        (
            'player',
            json = dict \
            (
                videoId = video_id,
            ),
        )

    def browse \
            (
                self,
                *,
                browse_id:    typing.Optional[str] = None,
                params:       typing.Optional[str] = None,
                continuation: typing.Optional[str] = None,
            ) -> types.Dict:
        return self \
        (
            'browse',
            params = types.Dict \
            (
                continuation = continuation,
                ctoken       = continuation,
            ).filter(),
            json = types.Dict \
            (
                browseId = browse_id,
                params   = params,
            ).filter(),
        )

    def search \
            (
                self,
                *,
                query:        typing.Optional[str] = None,
                params:       typing.Optional[str] = None,
                continuation: typing.Optional[str] = None,
            ) -> types.Dict:
        return self \
        (
            'search',
            params = types.Dict \
            (
                continuation = continuation,
                ctoken       = continuation,
            ).filter(),
            json = types.Dict \
            (
                query  = query or '',
                params = params,
            ).filter(),
        )

    def next \
            (
                self,
                *,
                video_id:     typing.Optional[str] = None,
                playlist_id:  typing.Optional[str] = None,
                params:       typing.Optional[str] = None,
                index:        typing.Optional[int] = None,
                continuation: typing.Optional[str] = None,
            ) -> types.Dict:
        return self \
        (
            'next',
            json = types.Dict \
            (
                params       = params,
                playlistId   = playlist_id,
                videoId      = video_id,
                index        = index,
                continuation = continuation,
            ).filter(),
        )

    def music_get_search_suggestions \
            (
                self,
                *,
                input: typing.Optional[None] = None,
            ) -> types.Dict:
        return self \
        (
            'music/get_search_suggestions',
            json = dict \
            (
                input = input or '',
            ),
        )

    def music_get_queue \
            (
                self,
                *,
                video_ids:   typing.Optional[typing.List[str]] = None,
                playlist_id: typing.Optional[str]              = None,
            ) -> types.Dict:
        return self \
        (
            'music/get_queue',
            json = types.Dict \
            (
                playlistId = playlist_id,
                videoIds   = video_ids or (None,),
            ).filter(),
        )

class InnerTube(BaseInnerTube):
    def __init__(self, client: enums.Client, locale: typing.Optional[models.Locale] = None):
        schema = infos.schemas[client]

        app = models.Application \
        (
            client   = infos.clients[client],
            service  = infos.services[schema.service],
            consumer = models.Consumer \
            (
                api    = infos.apis[enums.Api.YOUTUBEI_V1],
                device = infos.devices[schema.device],
            ),
        )

        adaptor = app.adaptor \
        (
            locale = locale,
        )

        session: sessions.Session = sessions.Session()

        session.base_url = adaptor.base_url

        session.headers.update(adaptor.headers)
        session.params.update(adaptor.params)
        session.context.update(adaptor.context)

        return super().__init__ \
        (
            session = session,
        )

class BaseSuggestQueries(BaseClient):
    def __call__(self, *args, **kwargs) -> types.Dict:
        return self.session.get(*args, **kwargs).json()

    def complete_search \
            (
                self,
                query:       str,
                *,
                client:      str,
                data_source: typing.Optional[str] = None,
                **kwargs,
            ) -> typing.List[str]:
        return self \
        (
            'complete/search',
            params = types.Dict \
            (
                **kwargs,
                client = client,
                q      = query,
                ds     = data_source,
                xhr    = enums.CharBool.TRUE.value,
                hjson  = enums.CharBool.TRUE.value,
            ).filter(),
        )

class SuggestQueries(BaseSuggestQueries):
    def __init__(self, locale: typing.Optional[models.Locale] = None):
        api    = infos.apis[enums.Api.SUGGEST_QUERIES]
        device = infos.devices[enums.Device.WEB]

        consumer = models.Consumer \
        (
            api    = infos.apis[enums.Api.SUGGEST_QUERIES],
            device = infos.devices[enums.Device.WEB],
        )

        session = sessions.BaseUrlSession()

        session.base_url = str(api)

        session.headers.update(consumer.headers(locale = locale))

        return super().__init__ \
        (
            session = session,
        )
