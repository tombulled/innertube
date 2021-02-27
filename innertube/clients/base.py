import functools
from ..adaptor import Adaptor
from ..infos.models import ClientInfo
from . import methods
from .decorators import method

@method(methods.config)
@method(methods.browse)
@method(methods.player)
class Client(object):
    adaptor: Adaptor

    def __init__(self, client_info: ClientInfo):
        self.adaptor = Adaptor(client_info)

    def __repr__(self):
        return '<Client(device={device_name!r}, service={service_name!r})>'.format \
        (
            device_name  = self.info.device.name,
            service_name = self.info.service.name,
        )

    @functools.wraps(Adaptor.dispatch)
    def __call__(self, *args, **kwargs):
        return self.adaptor.dispatch(*args, **kwargs)

    @property
    def info(self):
        return self.adaptor.client_info
