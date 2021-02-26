import functools

from ..adaptor import Adaptor
from ..infos.models import ClientInfo

class Client(object):
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

    def config(self):
        return self('config')

    def browse(self):
        ... # TODO: client('browse', payload = {'browseId': 'FE...'})

    def player(self):
        ... # TODO: client('player', payload = {'videoId': 'XXYlFuWEuKI'})

    def log_event(self):
        ... # TODO: client('log_event', payload = {'events': []})
