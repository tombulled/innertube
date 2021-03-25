import attr
import addict
import requests
import pydantic
import babel

import functools

from . import utils
from . import models
from . import sessions
from . import enums
from . import infos
from . import infos

from typing import \
(
    Callable,
    Optional,
    List,
)

def method(endpoint: str):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            return func \
            (
                functools.partial \
                (
                    self.session.post,
                    endpoint,
                ),
                *args,
                **kwargs,
            )

        return wrapper

    return decorator

@attr.s
class SessionWrapper(object):
    session: requests.Session = attr.ib()

class BaseClient(SessionWrapper):
    def __call__(self, *args, **kwargs):
        return self.session.post(*args, **kwargs)

    @method('config')
    def config(dispatch: Callable) -> addict.Dict:
        '''
        Dispatch the endpoint: config

        Retrieves config data
        '''

        return dispatch()

    @method('guide')
    def guide(dispatch: Callable) -> addict.Dict:
        '''
        Dispatch the endpoint: guide

        Retrieves guide data
        '''

        return dispatch()

    @method('player')
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

    @method('browse')
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
            params = utils.filter_kwargs \
            (
                continuation = continuation,
                ctoken       = continuation,
            ),
            json = utils.filter_kwargs \
            (
                browseId = browse_id,
                params   = params,
            ),
        )

    @method('search')
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
            params = utils.filter_kwargs \
            (
                continuation = continuation,
                ctoken       = continuation,
            ),
            json = utils.filter_kwargs \
            (
                query  = query or '',
                params = params,
            ),
        )

    @method('next')
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
            json = utils.filter_kwargs \
            (
                params       = params,
                playlistId   = playlist_id,
                videoId      = video_id,
                index        = index,
                continuation = continuation,
            ),
        )

    @method('music/get_search_suggestions')
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

    @method('music/get_queue')
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
            json = utils.filter_kwargs \
            (
                playlistId = playlist_id,
                videoIds   = video_ids or (None,),
            ),
        )

class Client(BaseClient):
    __info:   models.ClientInfo
    __locale: Optional[babel.Locale]

    def __init__(self, info: models.AppInfo, locale: babel.Locale = None):
        super().__init__ \
        (
            session = sessions.Session \
            (
                ** info.adaptor_info \
                (
                    locale = locale,
                ).dict(),
            )
        )

        self.__info   = info.client
        self.__locale = locale

    @classmethod
    def construct \
            (
                cls,
                service: enums.ServiceType,
                device:  enums.DeviceType,
                locale:  babel.Locale = None,
            ):
        return cls \
        (
            info = infos.apps.get \
            (
                service = infos.services.get(type = service),
                device  = infos.devices.get(type  = device),
            ),
            locale = locale,
        )

    def __repr__(self):
        return repr \
        (
            pydantic.create_model \
            (
                self.__class__.__name__,
                ** self.session.context,
            )(),
        )

    @property
    def info(self) -> models.ClientInfo:
        return self.__info

    @property
    def locale(self) -> babel.Locale:
        return self.__locale
