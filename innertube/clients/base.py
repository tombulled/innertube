import functools
from .. import adaptor
from ..infos import models

class Client(object):
    adaptor: adaptor.Adaptor

    def __init__(self, client_info: models.ClientInfo):
        self.adaptor = adaptor.Adaptor(client_info)

    def __repr__(self):
        return f'<Client(device={self.info.device.name!r}, service={self.info.service.name!r})>'

    @functools.wraps(adaptor.Adaptor.dispatch)
    def __call__(self, *args, **kwargs):
        return self.adaptor.dispatch(*args, **kwargs)

    @property
    def info(self):
        return self.adaptor.client_info
