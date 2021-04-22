import attr
import addict
import furl
import requests

import re
import typing
import operator
import functools

import register

from . import enums
from . import models
from . import parsers
from . import infos
from . import sessions
from . import utils

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

    def __call__(self, *args, **kwargs) -> addict.Dict:
        response = self.session.post(*args, **kwargs)

        response_data = addict.Dict(response.json())

        response_context: models.ResponseContext = parsers.response_context(response_data.responseContext)

        response_fingerprint = models.ResponseFingerprint \
        (
            request   = response_context.request.type,
            function  = response_context.function,
            browse_id = response_context.browse_id,
            context   = response_context.context,
            client    = response_context.client.name,
            endpoint  = '/'.join(furl.furl(response.url).path.segments[2:]),
        )

        response_schema = models.Parser.from_model(response_fingerprint)

        for parser, schema in reversed(self.parsers.items()):
            if (schema & response_schema).any():
                return parser(response_data)

        # TODO: Raise appropriate exception
        raise Exception(f'No parser found for context: {response_context!s}')

    def config(self) -> addict.Dict:
        return self('config')

    def guide(self) -> addict.Dict:
        return self('guide')

    def player(self, *, video_id: str) -> addict.Dict:
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
                browse_id:    typing.Optional[str] = None,
                *,
                params:       typing.Optional[str] = None,
                continuation: typing.Optional[str] = None,
            ) -> addict.Dict:
        return self \
        (
            'browse',
            params = utils.filter \
            (
                continuation = continuation,
                ctoken       = continuation,
            ),
            json = utils.filter \
            (
                browseId = browse_id,
                params   = params,
            ),
        )

    def search \
            (
                self,
                *,
                query:        typing.Optional[str] = None,
                params:       typing.Optional[str] = None,
                continuation: typing.Optional[str] = None,
            ) -> addict.Dict:
        return self \
        (
            'search',
            params = addict.Dict \
            (
                continuation = continuation,
                ctoken       = continuation,
            ).filter(),
            json = addict.Dict \
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
            ) -> addict.Dict:
        return self \
        (
            'next',
            json = addict.Dict \
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
            ) -> addict.Dict:
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
            ) -> addict.Dict:
        return self \
        (
            'music/get_queue',
            json = addict.Dict \
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
            client  = infos.clients[client],
            service = infos.services[schema.service],
            device  = infos.devices[schema.device],
            api     = infos.apis[enums.Api.YOUTUBEI],
            company = infos.companies[enums.Company.GOOGLE],
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
    def __call__(self, *args, **kwargs) -> addict.Dict:
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
            params = addict.Dict \
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
