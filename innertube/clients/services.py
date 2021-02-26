from . import base
from .. import utils
from typing import Union, List

class YouTubeClient(base.Client):
    def guide(self):
        return self('guide')

    def search \
            (
                self,
                *,
                query:        Union[str, None] = None,
                params:       Union[str, None] = None,
                continuation: Union[str, None] = None,
            ) -> dict:
        return self \
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
                self,
                video_id:     str    = None,
                playlist_id:  str    = None,
                params:       str    = None, # For 'radio' mode etc.
                index:        int    = None, # Potentially not needed?
                continuation: str    = None,
            ) -> dict:
        return self \
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

class YouTubeMusicClient(base.Client):
    def guide(self):
        return self('guide')

    def search \
            (
                self,
                *,
                query:        Union[str, None] = None,
                params:       Union[str, None] = None,
                continuation: Union[str, None] = None,
            ):
        return self \
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
                self,
                video_id:     str    = None,
                playlist_id:  str    = None,
                params:       str    = None, # For 'radio' mode etc.
                index:        int    = None, # Potentially not needed?
                continuation: str    = None,
            ) -> dict:
        return self \
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

    def music_get_search_suggestions(self, *, input: Union[str, None]):
        return self \
        (
            'music/get_search_suggestions',
            payload = \
            {
                'input': input or '',
            },
        )

    def music_get_queue(self, *, video_ids: Union[List[str], None] = None, playlist_id: Union[str, None] = None):
        return self \
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

class YouTubeKidsClient(base.Client):
    pass

class YouTubeStudioClient(base.Client):
    pass
