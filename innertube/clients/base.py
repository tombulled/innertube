'''
Library containing the base InnerTube `Client` class

>>> from innertube.clients.base import Client
>>>
>>> Client
<class 'innertube.clients.base.Client'>
>>>
'''

import functools
from ..adaptor import Adaptor
from ..infos.models import ClientInfo
from . import methods
from .decorators import method

@method(methods.config)
@method(methods.browse)
@method(methods.player)
class Client(object):
    '''
    Base InnerTube Client

    Attributes:
        adaptor: Adaptor

    Properties:
        info: ClientInfo
    '''

    adaptor: Adaptor

    def __init__(self, client_info: ClientInfo):
        '''
        Initialise the Client

        Creates and stores an `Adaptor` for dispatching requests
        '''

        self.adaptor = Adaptor(client_info)

    def __repr__(self) -> str:
        '''
        Return a string representation of the Client
        '''

        return '<Client(device={device_name!r}, service={service_name!r})>'.format \
        (
            device_name  = self.info.device.name,
            service_name = self.info.service.name,
        )

    @functools.wraps(Adaptor.dispatch)
    def __call__(self, *args, **kwargs) -> dict:
        '''
        Short-hand for dispatching requests through the adaptor instance
        '''

        return self.adaptor.dispatch(*args, **kwargs)

    @property
    def info(self) -> ClientInfo:
        '''
        Property to return the Adaptor's ClientInfo
        '''

        return self.adaptor.client_info
