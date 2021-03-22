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
import addict

from . import utils
from . import constants
from . import apps

from typing import \
(
    List,
)

from babel import \
(
    Locale,
)

from .infos.models import \
(
    AppInfo,
)

def complete_search \
        (
            query: str,
            *,
            app:     AppInfo = None,
            locale:  Locale  = None,
        ) -> List[str]:
    '''
    Dispatch a 'complete/search' request to suggestqueries.google.com

    Reccomended devices for services:
        YouTube:      Tv
        YouTubeMusic: Android
        YouTubeKids:  Web
    '''

    if not app:
        app = apps.Tv

    if not locale:
        locale = constants.DEFAULT_LOCALE

    assert app.client.identifier, 'Client has no identifier'

    response = requests.get \
    (
        url = utils.url \
        (
            domain   = 'suggestqueries.google.com',
            endpoint = 'complete/search',
        ),
        params = utils.filter \
        (
            dict \
            (
                client = app.client.identifier,
                q      = query,
                hl     = locale.language,
                gl     = locale.territory,
                ds     = 'yt',
                oe     = 'utf-8',
                xhr    = 't',
                hjson  = 't',
            ),
        ),
        headers = \
        {
            'User-Agent': app.user_agent,
        },
    )

    return \
    [
        suggestion
        for suggestion, _ in response.json()[1]
    ]
