'''
Library containing the base InnerTube `Client` class

>>> from innertube.clients.base import Client
>>>
>>> Client
<class 'innertube.clients.base.Client'>
>>>
'''

import babel
import functools

from . import methods

from .decorators import method

from ..adaptor import \
(
    Adaptor,
)

from ..infos.models import \
(
    ClientInfo,
)

from babel import \
(
    Locale,
)

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

    def __init__ \
            (
                self,
                client_info: ClientInfo,
                *,
                locale: Locale = None,
            ):
        '''
        Initialise the Client

        Creates and stores an `Adaptor` for dispatching requests
        '''

        self.adaptor = Adaptor \
        (
            client_info,
            locale = locale,
        )

    def __repr__(self) -> str:
        '''
        Return a string representation of the Client
        '''

        return '<Client({params})>'.format \
        (
            params = ', '.join \
            (
                f'{key}={value!r}'
                for key, value in \
                {
                    'device':  self.info.device.name,
                    'service': self.info.service.name,
                    'locale':  self.adaptor.client_context.hl,
                }.items()
            )
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
