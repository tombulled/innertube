'''
Library containing InnerTube methods. These functions are responsible for
interacting with the various endpoints used by the InnerTube API

Usage:
    >>> from innertube import methods
    >>>
    >>> dir(methods)
    ...
    >>>
    >>> methods.config
    <function config at 0x7fd548674940>
    >>>
'''

from .. import utils
from typing import Union, Callable, List

def config(dispatch: Callable) -> dict:
    '''
    Dispatch the endpoint: config

    Retrieves config data
    '''

    return dispatch('config')

def guide(dispatch: Callable) -> dict:
    '''
    Dispatch the endpoint: guide

    Retrieves guide data
    '''

    return dispatch('guide')

def player(dispatch: Callable, *, video_id: str) -> dict:
    '''
    Dispatch the endpoint: player

    Retrieves player data
    '''

    return dispatch \
    (
        'player',
        payload = \
        {
            'videoId': video_id,
        }
    )

def browse \
        (
            dispatch: Callable,
            *,
            browse_id:    Union[None, str] = None,
            params:       Union[None, str] = None,
            continuation: Union[None, str] = None,
        ) -> dict:
    '''
    Dispatch the endpoint: browse

    Retrieves browse data
    '''

    return dispatch \
    (
        'browse',
        params = utils.filter \
        (
            {
                'continuation': continuation,
                'ctoken':       continuation,
            }
        ),
        payload = utils.filter \
        (
            {
                'browseId': browse_id,
                'params':   params,
            }
        ),
    )

def search \
        (
            dispatch: Callable,
            *,
            query:        Union[None, str] = None,
            params:       Union[None, str] = None,
            continuation: Union[None, str] = None,
        ) -> dict:
    '''
    Dispatch the endpoint: search

    Retrieves search data
    '''

    return dispatch \
    (
        'search',
        params = utils.filter \
        (
            {
                'continuation': continuation,
                'ctoken':       continuation,
            }
        ),
        payload = utils.filter \
        (
            {
                'query':  query or '',
                'params': params,
            }
        ),
    )

def next \
        (
            dispatch: Callable,
            *,
            video_id:     Union[None, str] = None,
            playlist_id:  Union[None, str] = None,
            params:       Union[None, str] = None,
            index:        Union[None, int] = None,
            continuation: Union[None, str] = None,
        ) -> dict:
    '''
    Dispatch the endpoint: next

    Retrieves next data
    '''

    return dispatch \
    (
        'next',
        payload = utils.filter \
        (
            {
                'params':       params,
                'playlistId':   playlist_id,
                'videoId':      video_id,
                'index':        index,
                'continuation': continuation,
            }
        ),
    )

def music_get_search_suggestions \
        (
            dispatch: Callable,
            *,
            input: Union[str, None] = None,
        ) -> dict:
    '''
    Dispatch the endpoint: music/get_search_suggestions

    Retrieves music search suggestions data
    '''

    return dispatch \
    (
        'music/get_search_suggestions',
        payload = \
        {
            'input': input or '',
        },
    )

def music_get_queue \
        (
            dispatch: Callable,
            *,
            video_ids:   Union[None, List[str]] = None,
            playlist_id: Union[None, str]       = None,
        ) -> dict:
    '''
    Dispatch the endpoint: music/get_queue

    Retrieves music queue data
    '''

    return dispatch \
    (
        'music/get_queue',
        payload = utils.filter \
        (
            {
                'playlistId': playlist_id,
                'videoIds':   video_ids or (None,),
            }
        )
    )
