import attr
import addict
import toolz

import register

import abc
import typing
import functools

from . import sessions
from . import utils
from . import enums
from . import models
from . import errors

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class BaseClient(abc.ABC):
    session: sessions.BaseSession = attr.ib()

    @abc.abstractmethod
    def __call__(self):
        raise NotImplementedError

    def __attrs_post_init__(self):
        pass

@attrs
class BaseSuggestQueriesClient(BaseClient):
    session: sessions.SuggestQueriesSession = attr.ib \
    (
        default = attr.Factory(sessions.SuggestQueriesSession),
        init    = False,
    )

    def __call__(self, *args, **kwargs):
        return self.session.get(*args, **kwargs).json()

@attrs
class BaseInnerTubeClient(BaseClient):
    session: sessions.InnerTubeSession = attr.ib \
    (
        default = attr.Factory(sessions.InnerTubeSession),
        init    = False,
    )

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
        init = False,
    )

    def __attrs_post_init__(self):
        self.parsers()(toolz.identity)

    def __call__(self, *args, **kwargs) -> addict.Dict:
        response = self.session.post(*args, **kwargs)

        response_data = addict.Dict(response.json())

        fingerprint = models.ResponseFingerprint.from_response(response)

        parser = models.Parser.from_model(fingerprint)

        if response_data.responseContext:
            del response_data.responseContext

        for parse, schema in reversed(self.parsers.items()):
            if not schema.any() or (schema & parser).any():
                return parse(response_data)

        raise errors.NoParserFound(f'No parser found for response with fingerprint: {fingerprint!r}')

@attrs
class SuggestQueriesClient(BaseSuggestQueriesClient):
    def complete_search \
            (
                self,
                query:       str,
                *,
                client:      str,
                data_source: typing.Optional[str] = None,
            ) -> typing.List[str]:
        return self \
        (
            'complete/search',
            params = utils.filter \
            (
                client = client,
                q      = query,
                ds     = data_source,
                xhr    = enums.Bool.TRUE.value,
                hjson  = enums.Bool.TRUE.value,
            ),
        )

@attrs
class InnerTubeClient(BaseInnerTubeClient):
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
                query:        typing.Optional[str] = None,
                *,
                params:       typing.Optional[str] = None,
                continuation: typing.Optional[str] = None,
            ) -> addict.Dict:
        return self \
        (
            'search',
            params = utils.filter \
            (
                continuation = continuation,
                ctoken       = continuation,
            ),
            json = utils.filter \
            (
                query  = query or '',
                params = params,
            ),
        )

    def next \
            (
                self,
                video_id:     typing.Optional[str] = None,
                playlist_id:  typing.Optional[str] = None,
                *,
                params:       typing.Optional[str] = None,
                index:        typing.Optional[int] = None,
                continuation: typing.Optional[str] = None,
            ) -> addict.Dict:
        return self \
        (
            'next',
            json = utils.filter \
            (
                params       = params,
                playlistId   = playlist_id,
                videoId      = video_id,
                index        = index,
                continuation = continuation,
            ),
        )

    def music_get_search_suggestions \
            (
                self,
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
            json = utils.filter \
            (
                playlistId = playlist_id,
                videoIds   = video_ids or (None,),
            ),
        )
