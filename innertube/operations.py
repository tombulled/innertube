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
import furl

from . import utils
from . import constants
from . import apps
from . import enums

from typing import \
(
    List,
)

from babel import \
(
    Locale,
)

from .models import \
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

    # Note: This needs updating!
    if not app:
        app = apps.YouTubeTv

    assert app.client.identifier, 'Client has no identifier'

    response = requests.get \
    (
        url = furl.furl \
        (
            scheme = enums.Scheme.HTTPS.value,
            host   = 'suggestqueries.google.com',
            path   = 'complete/search',
        ),
        params = utils.filtered_dict \
        (
            client = app.client.identifier,
            q      = query,
            hl     = locale and locale.language,
            gl     = locale and locale.territory,
            ds     = 'yt',
            oe     = 'utf-8',
            xhr    = 't',
            hjson  = 't',
        ),
        headers = \
        {
            enums.Header.USER_AGENT.value: app.user_agent,
        },
    )

    return \
    [
        suggestion
        for suggestion, _ in response.json()[1]
    ]
