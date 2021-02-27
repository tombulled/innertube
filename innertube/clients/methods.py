from .. import utils
from typing import Union, Callable, List

def config(dispatch: Callable):
    return dispatch('config')

def guide(dispatch: Callable):
    return dispatch('guide')

def player(dispatch: Callable, video_id: str):
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
            browse_id:    Union[str, None] = None,
            params:       Union[str, None] = None,
            continuation: Union[str, None] = None,
        ):
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
            query:        Union[str, None] = None,
            params:       Union[str, None] = None,
            continuation: Union[str, None] = None,
        ) -> dict:
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
            video_id:     str    = None, # NOTE: These should all use typing.Union
            playlist_id:  str    = None,
            params:       str    = None, # For 'radio' mode etc.
            index:        int    = None, # Potentially not needed?
            continuation: str    = None,
        ) -> dict:
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

def music_get_search_suggestions(dispatch: Callable, *, input: Union[str, None]):
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
            video_ids: Union[List[str], None] = None,
            playlist_id: Union[str, None] = None,
        ):
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
