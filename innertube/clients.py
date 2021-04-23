import attr
import addict
import furl
import requests

import register

import re
import abc
import typing
import operator
import functools

from . import enums
from . import models
from . import parsers
from . import infos
from . import sessions
from . import utils
from . import adaptors

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class BaseClient(object):
    adaptor: adaptors.Adaptor = attr.ib \
    (
        default = attr.Factory(adaptors.Adaptor),
    )

    def __call__(self, *args, **kwargs):
        return self.adaptor(*args, **kwargs)

@attrs
class BaseSuggestQueriesClient(BaseClient):
    adaptor: adaptors.SuggestQueriesAdaptor = attr.ib \
    (
        default = attr.Factory(adaptors.SuggestQueriesAdaptor),
    )

@attrs
class BaseInnerTubeClient(BaseClient):
    adaptor: adaptors.InnerTubeAdaptor = attr.ib \
    (
        default = attr.Factory(adaptors.InnerTubeAdaptor),
    )

@attrs
class SuggestQueriesClient(BaseSuggestQueriesClient):
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
            params = utils.filter \
            (
                **kwargs,
                client = client,
                q      = query,
                ds     = data_source,
                xhr    = enums.CharBool.TRUE.value,
                hjson  = enums.CharBool.TRUE.value,
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
