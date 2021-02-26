import functools

from ..adaptor import Adaptor
from ..infos.models import ClientInfo

from typing import Union

class BaseClient(object):
    adaptor: Adaptor

    def __init__(self, client_info: ClientInfo):
        self.adaptor = Adaptor(client_info)

    def __repr__(self):
        return f'<Client(device={self.info.device.name!r}, service={self.info.service.name!r})>'

    @functools.wraps(Adaptor.dispatch)
    def __call__(self, *args, **kwargs):
        return self.adaptor.dispatch(*args, **kwargs)

    @property
    def info(self):
        return self.adaptor.client_info

class Client(BaseClient):
    def config(self):
        return self('config')

    def browse \
            (
                self,
                *,
                browse_id:    Union[str, None] = None,
                params:       Union[str, None] = None,
                continuation: Union[str, None] = None,
            ):
        return self.dispatch \
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

    def player(self, video_id: str):
        return self \
        (
            'player',
            payload = \
            {
                'videoId': video_id,
            }
        )
