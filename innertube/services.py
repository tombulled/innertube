'''
Library containing info object instances of type: ServiceInfo

Usage:
    >>> from innertube import services
    >>>
    >>> dir(services)
    ...
    >>>
    >>> services.YouTube
    ServiceInfo(...)
    >>>
'''

from . import models
from . import enums

YouTube = models.ServiceInfo \
(
    name      = 'YouTube',
    domain    = 'www.youtube.com',
    id        = 1,
    endpoints = \
    [
        enums.ApiEndpoint.CONFIG,
        enums.ApiEndpoint.BROWSE,
        enums.ApiEndpoint.PLAYER,
        enums.ApiEndpoint.GUIDE,
        enums.ApiEndpoint.SEARCH,
        enums.ApiEndpoint.NEXT,
    ],
)

YouTubeMusic = models.ServiceInfo \
(
    name      = 'YouTube Music',
    domain    = 'music.youtube.com',
    id        = 67,
    endpoints = \
    [
        enums.ApiEndpoint.CONFIG,
        enums.ApiEndpoint.BROWSE,
        enums.ApiEndpoint.PLAYER,
        enums.ApiEndpoint.GUIDE,
        enums.ApiEndpoint.SEARCH,
        enums.ApiEndpoint.NEXT,
        enums.ApiEndpoint.MUSIC_GET_SEARCH_SUGGESTIONS,
        enums.ApiEndpoint.MUSIC_GET_QUEUE,
    ],
)

YouTubeKids = models.ServiceInfo \
(
    name      = 'YouTube Kids',
    domain    = 'www.youtubekids.com',
    id        = 76,
    endpoints = \
    [
        enums.ApiEndpoint.CONFIG,
        enums.ApiEndpoint.BROWSE,
        enums.ApiEndpoint.PLAYER,
        enums.ApiEndpoint.SEARCH,
        enums.ApiEndpoint.NEXT,
    ],
)

YouTubeStudio = models.ServiceInfo \
(
    name      = 'YouTube Studio',
    domain    = 'studio.youtube.com',
    id        = 62,
    endpoints = \
    [
        enums.ApiEndpoint.CONFIG,
        enums.ApiEndpoint.BROWSE,
        enums.ApiEndpoint.PLAYER,
    ],
)
