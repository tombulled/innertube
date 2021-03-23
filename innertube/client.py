import attr
import addict
import requests

from . import utils
from . import decorators
from . import enums

from typing import \
(
    Callable,
    Optional,
    List,
)

@attr.s(frozen = True)
class SessionWrapper(object):
    session: requests.Session = attr.ib()

class Client(SessionWrapper):
    def __call__(self, *args, **kwargs):
        return self.session.post(*args, **kwargs)

    @decorators.method(enums.Endpoint.CONFIG)
    def config(dispatch: Callable) -> addict.Dict:
        '''
        Dispatch the endpoint: config

        Retrieves config data
        '''

        return dispatch()

    @decorators.method(enums.Endpoint.GUIDE)
    def guide(dispatch: Callable) -> addict.Dict:
        '''
        Dispatch the endpoint: guide

        Retrieves guide data
        '''

        return dispatch()

    @decorators.method(enums.Endpoint.PLAYER)
    def player(dispatch: Callable, *, video_id: str) -> addict.Dict:
        '''
        Dispatch the endpoint: player

        Retrieves player data
        '''

        return dispatch \
        (
            json = dict \
            (
                videoId = video_id,
            ),
        )

    @decorators.method(enums.Endpoint.BROWSE)
    def browse \
            (
                dispatch: Callable,
                *,
                browse_id:    Optional[str] = None,
                params:       Optional[str] = None,
                continuation: Optional[str] = None,
            ) -> addict.Dict:
        '''
        Dispatch the endpoint: browse

        Retrieves browse data
        '''

        return dispatch \
        (
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

    @decorators.method(enums.Endpoint.SEARCH)
    def search \
            (
                dispatch: Callable,
                *,
                query:        Optional[str] = None,
                params:       Optional[str] = None,
                continuation: Optional[str] = None,
            ) -> addict.Dict:
        '''
        Dispatch the endpoint: search

        Retrieves search data
        '''

        return dispatch \
        (
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

    @decorators.method(enums.Endpoint.NEXT)
    def next \
            (
                dispatch: Callable,
                *,
                video_id:     Optional[str] = None,
                playlist_id:  Optional[str] = None,
                params:       Optional[str] = None,
                index:        Optional[int] = None,
                continuation: Optional[str] = None,
            ) -> addict.Dict:
        '''
        Dispatch the endpoint: next

        Retrieves next data
        '''

        return dispatch \
        (
            json = utils.filter \
            (
                params       = params,
                playlistId   = playlist_id,
                videoId      = video_id,
                index        = index,
                continuation = continuation,
            ),
        )

    @decorators.method(enums.Endpoint.MUSIC_GET_SEARCH_SUGGESTIONS)
    def music_get_search_suggestions \
            (
                dispatch: Callable,
                *,
                input: Optional[None] = None,
            ) -> addict.Dict:
        '''
        Dispatch the endpoint: music/get_search_suggestions

        Retrieves music search suggestions data
        '''

        return dispatch \
        (
            json = dict \
            (
                input = input or '',
            ),
        )

    @decorators.method(enums.Endpoint.MUSIC_GET_QUEUE)
    def music_get_queue \
            (
                dispatch: Callable,
                *,
                video_ids:   Optional[List[str]] = None,
                playlist_id: Optional[str]       = None,
            ) -> addict.Dict:
        '''
        Dispatch the endpoint: music/get_queue

        Retrieves music queue data
        '''

        return dispatch \
        (
            json = utils.filter \
            (
                playlistId = playlist_id,
                videoIds   = video_ids or (None,),
            ),
        )
