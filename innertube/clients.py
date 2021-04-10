import attr
import addict
import requests

import typing

@attr.s
class SessionWrapper(object):
    session: requests.Session = attr.ib()

class BaseClient(SessionWrapper):
    def __call__(self, *args, **kwargs) -> addict.Dict:
        return addict.Dict(self.session.post(*args, **kwargs).json())

class Client(BaseClient):
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
                *,
                browse_id:    typing.Optional[str] = None,
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
                playlist_id: typing.Optional[str]       = None,
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
