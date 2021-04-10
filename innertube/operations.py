import requests
import addict
import furl
import babel

import typing

from . import enums
from . import utils
from . import infos
from . import sessions

def complete_search \
        (
            *,
            query:  str,
            client: typing.Optional[str]          = None,
            locale: typing.Optional[babel.Locale] = None,
        ) -> typing.List[str]:
    '''
    Dispatch a 'complete/search' request to suggestqueries.google.com

    Notes:
        * `client` refers to a Client.identifier string

    Reccomended devices for services:
        YouTube:      Tv
        YouTubeMusic: Android
        YouTubeKids:  Web
    '''

    app = infos.apps[enums.App.YOUTUBE_TV]
    api = infos.apis[enums.Api.SUGGEST_QUERIES]

    session = sessions.BaseUrlSession \
    (
        base_url = str(api),
    )

    response = session.get \
    (
        'complete/search',
        params = utils.filter \
        (
            client = client or app.client.identifier,
            q      = query,
            hl     = locale and locale.language,
            gl     = locale and locale.territory,
            ds     = enums.DataSource.YOUTUBE,
            oe     = enums.Encoding.UTF_8,
            xhr    = enums.CharBool.TRUE,
            hjson  = enums.CharBool.TRUE,
        ),
        headers = \
        {
            enums.Header.USER_AGENT.value: str(app.user_agent()),
        },
    )

    return \
    [
        suggestion
        for suggestion, *_ in response.json()[1]
    ]
