from . import models
from . import types

YouTube = models.ServiceInfo \
(
    name   = 'YouTube',
    type   = types.ServiceType.YouTube,
    domain = 'www.youtube.com',
    id     = 1,
)

YouTubeMusic = models.ServiceInfo \
(
    name   = 'YouTube Music',
    type   = types.ServiceType.YouTubeMusic,
    domain = 'music.youtube.com',
    id     = 67,
)

YouTubeKids = models.ServiceInfo \
(
    name   = 'YouTube Kids',
    type   = types.ServiceType.YouTubeKids,
    domain = 'www.youtubekids.com',
    id     = 76,
)

YouTubeStudio = models.ServiceInfo \
(
    name   = 'YouTube Studio',
    type   = types.ServiceType.YouTubeStudio,
    domain = 'studio.youtube.com',
    id     = 62,
)
