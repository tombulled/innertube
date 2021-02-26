from . import info
from . import types

YouTube = info.ServiceInfo \
(
    name   = 'YouTube',
    type   = types.ServiceType.YouTube,
    domain = 'www.youtube.com',
    packages = \
    {
        types.DeviceType.Android: 'com.google.android.youtube',
        types.DeviceType.Ios:     'com.google.ios.youtube',
    },
)

YouTubeMusic = info.ServiceInfo \
(
    name   = 'YouTube Music',
    type   = types.ServiceType.YouTubeMusic,
    domain = 'music.youtube.com',
    packages = \
    {
        types.DeviceType.Android: 'com.google.android.apps.youtube.music',
        types.DeviceType.Ios:     'com.google.ios.youtubemusic',
    },
)

YouTubeKids = info.ServiceInfo \
(
    name   = 'YouTube Kids',
    type   = types.ServiceType.YouTubeKids,
    domain = 'www.youtubekids.com',
    packages = \
    {
        types.DeviceType.Android: 'com.google.android.apps.youtube.kids',
        types.DeviceType.Ios:     'com.google.ios.youtubekids',
    },
)

YouTubeStudio = info.ServiceInfo \
(
    name   = 'YouTube Studio',
    type   = types.ServiceType.YouTubeStudio,
    domain = 'studio.youtube.com',
    packages = \
    {
        types.DeviceType.Android: 'com.google.android.apps.youtube.creator',
        types.DeviceType.Ios:     'com.google.ios.ytcreator',
    },
)
