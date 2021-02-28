'''
Library containing non-innertube related operations that are used by the various services

These operations do not go through the InnerTube API and are included for convenience

Usage:
    >>> from innertube import operations
    >>>
    >>> dir(operations)
    ...
    >>>
    >>> operations.complete_search
    <function complete_search at 0x7fd5476ec670>
    >>>
'''

import requests
from typing import Union, List
from . import utils
from .infos.types import ServiceType
from .infos.models import ServiceInfo

def complete_search \
        (
            query: str,
            *,
            service: Union[ServiceInfo, ServiceType] = ServiceType.YouTube,
        ) -> List[str]:
    '''
    Dispatch a 'complete/search' request to suggestqueries.google.com
    '''

    service_type = service if isinstance(service, ServiceType) else service.type

    clients = \
    {
        ServiceType.YouTube:      'youtube-lr',               # Device: Tv
        ServiceType.YouTubeMusic: 'youtube-music-android-v2', # Device: Android
        ServiceType.YouTubeKids:  'youtube-pegasus-web',      # Device: Web
    }

    if service_type not in clients:
        service_type = ServiceType.YouTube

    response = requests.get \
    (
        url = utils.url \
        (
            domain   = 'suggestqueries.google.com',
            endpoint = 'complete/search',
        ),
        params = \
        {
            'client': clients.get(service_type),
            'q':      query,
            'hl':     'en',
            'gl':     'gb',
            'ds':     'yt',
            'oe':     'utf-8',
            'xhr':    't',
        },
    )

    return [suggestion for suggestion, _ in response.json()[1]]
