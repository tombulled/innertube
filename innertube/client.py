'''
Library containing the base InnerTube `Client` class
'''

import babel
import functools

from . import utils

from .decorators import \
(
    method,
)

from .enums import \
(
    ApiEndpoint,
)

from .adaptor import \
(
    Adaptor,
)

from .models import \
(
    AppInfo,
)

from typing import \
(
    Callable,
    Optional,
    List,
)

from babel import \
(
    Locale,
)

class Client(object):
    '''
    Base InnerTube Client

    Attributes:
        adaptor: Adaptor

    Properties:
        info: AppInfo
    '''

    adaptor: Adaptor

    def __init__ \
            (
                self,
                info: AppInfo,
                *,
                locale: Locale = None,
            ):
        '''
        Initialise the Client

        Creates and stores an `Adaptor` for dispatching requests
        '''

        super().__init__()

        self.adaptor = Adaptor \
        (
            info,
            locale = locale,
        )

    def __repr__(self) -> str:
        '''
        Return a string representation of the Client
        '''

        return utils.repr \
        (
            class_name = self.__class__.__mro__[-2].__name__,
            fields     = dict \
            (
                service = self.info.service.name,
                device  = self.info.device.name,
                locale  = self.adaptor.context.hl,
            ),
        )

    @functools.wraps(Adaptor.dispatch)
    def __call__(self, *args, **kwargs) -> dict:
        '''
        Short-hand for dispatching requests through the adaptor instance
        '''

        return self.adaptor.dispatch(*args, **kwargs)

    @property
    def info(self) -> AppInfo:
        '''
        Property to return the Adaptor's AppInfo
        '''

        return self.adaptor.info

    @method(ApiEndpoint.CONFIG)
    def config(dispatch: Callable) -> dict:
        '''
        Dispatch the endpoint: config

        Retrieves config data
        '''

        return dispatch()

    @method(ApiEndpoint.GUIDE)
    def guide(dispatch: Callable) -> dict:
        '''
        Dispatch the endpoint: guide

        Retrieves guide data
        '''

        return dispatch()

    @method(ApiEndpoint.PLAYER)
    def player(dispatch: Callable, *, video_id: str) -> dict:
        '''
        Dispatch the endpoint: player

        Retrieves player data
        '''

        return dispatch \
        (
            payload = dict \
            (
                videoId = video_id,
            ),
        )

    @method(ApiEndpoint.BROWSE)
    def browse \
            (
                dispatch: Callable,
                *,
                browse_id:    Optional[str] = None,
                params:       Optional[str] = None,
                continuation: Optional[str] = None,
            ) -> dict:
        '''
        Dispatch the endpoint: browse

        Retrieves browse data
        '''

        return dispatch \
        (
            params = utils.filter \
            (
                dict \
                (
                    continuation = continuation,
                    ctoken       = continuation,
                ),
            ),
            payload = utils.filter \
            (
                dict \
                (
                    browseId = browse_id,
                    params   = params,
                ),
            ),
        )

    @method(ApiEndpoint.SEARCH)
    def search \
            (
                dispatch: Callable,
                *,
                query:        Optional[str] = None,
                params:       Optional[str] = None,
                continuation: Optional[str] = None,
            ) -> dict:
        '''
        Dispatch the endpoint: search

        Retrieves search data
        '''

        return dispatch \
        (
            params = utils.filter \
            (
                dict \
                (
                    continuation = continuation,
                    ctoken       = continuation,
                ),
            ),
            payload = utils.filter \
            (
                dict \
                (
                    query  = query or '',
                    params = params,
                ),
            ),
        )

    @method(ApiEndpoint.NEXT)
    def next \
            (
                dispatch: Callable,
                *,
                video_id:     Optional[str] = None,
                playlist_id:  Optional[str] = None,
                params:       Optional[str] = None,
                index:        Optional[int] = None,
                continuation: Optional[str] = None,
            ) -> dict:
        '''
        Dispatch the endpoint: next

        Retrieves next data
        '''

        return dispatch \
        (
            payload = utils.filter \
            (
                dict \
                (
                    params       = params,
                    playlistId   = playlist_id,
                    videoId      = video_id,
                    index        = index,
                    continuation = continuation,
                ),
            ),
        )

    @method(ApiEndpoint.MUSIC_GET_SEARCH_SUGGESTIONS)
    def music_get_search_suggestions \
            (
                dispatch: Callable,
                *,
                input: Optional[None] = None,
            ) -> dict:
        '''
        Dispatch the endpoint: music/get_search_suggestions

        Retrieves music search suggestions data
        '''

        return dispatch \
        (
            payload = dict \
            (
                input = input or '',
            ),
        )

    @method(ApiEndpoint.MUSIC_GET_QUEUE)
    def music_get_queue \
            (
                dispatch: Callable,
                *,
                video_ids:   Optional[List[str]] = None,
                playlist_id: Optional[str]       = None,
            ) -> dict:
        '''
        Dispatch the endpoint: music/get_queue

        Retrieves music queue data
        '''

        return dispatch \
        (
            payload = utils.filter \
            (
                dict \
                (
                    playlistId = playlist_id,
                    videoIds   = video_ids or (None,),
                ),
            ),
        )
