import pydantic

import enum
import collections

from . import models
from . import enums

from typing import \
(
    List,
    Optional
)

class Container(collections.UserList):
    def __init__(self, *args):
        super().__init__(args)

    def search(self, **kwargs):
        return \
        [
            item
            for item in self
            if all \
            (
                getattr(item, key, None) == value
                for key, value in kwargs.items()
            )
        ]

    def get(self, **kwargs):
        if (results := self.search(**kwargs)):
            return results[0]

clients = Container \
(
    models.ClientInfo \
    (
        type       = enums.ClientType.WEB,
        name       = 'WEB',
        version    = '2.20210223.09.00',
        identifier = 'youtube',
    ),
    models.ClientInfo \
    (
        type    = enums.ClientType.WEB_MUSIC,
        name    = 'WEB_REMIX',
        version = '0.1',
    ),
    models.ClientInfo \
    (
        type       = enums.ClientType.WEB_KIDS,
        name       = 'WEB_KIDS',
        version    = '2.1.3',
        identifier = 'youtube-pegasus-web',
    ),
    models.ClientInfo \
    (
        type    = enums.ClientType.WEB_STUDIO,
        name    = 'WEB_CREATOR',
        version = '1.20210223.01.00',
    ),
    models.ClientInfo \
    (
        type    = enums.ClientType.ANDROID,
        name    = 'ANDROID',
        version = '16.07.34',
    ),
    models.ClientInfo \
    (
        type       = enums.ClientType.ANDROID_MUSIC,
        name       = 'ANDROID_MUSIC',
        version    = '4.16.51',
        identifier = 'youtube-music-android',
    ),
    models.ClientInfo \
    (
        type    = enums.ClientType.ANDROID_KIDS,
        name    = 'ANDROID_KIDS',
        version = '6.02.3',
    ),
    models.ClientInfo \
    (
        type    = enums.ClientType.ANDROID_STUDIO,
        name    = 'ANDROID_CREATOR',
        version = '21.06.103',
    ),
    models.ClientInfo \
    (
        type    = enums.ClientType.IOS,
        name    = 'IOS',
        version = '16.05.7',
    ),
    models.ClientInfo \
    (
        type       = enums.ClientType.IOS_MUSIC,
        name       = 'IOS_MUSIC',
        version    = '4.16.1',
        identifier = 'youtube-music-ios',
    ),
    models.ClientInfo \
    (
        type    = enums.ClientType.IOS_KIDS,
        name    = 'IOS_KIDS',
        version = '5.42.2',
    ),
    models.ClientInfo \
    (
        type    = enums.ClientType.IOS_STUDIO,
        name    = 'IOS_CREATOR',
        version = '20.47.100',
    ),
    models.ClientInfo \
    (
        type       = enums.ClientType.TV,
        name       = 'TVHTML5',
        version    = '7.20210224.00.00',
        identifier = 'youtube-lr',
    ),
)

devices = Container \
(
    models.DeviceInfo \
    (
        type    = enums.DeviceType.WEB,
        name    = 'Web',
        product = models.ProductInfo \
        (
            name    = 'Mozilla',
            version = '5.0',
            token   = 'Windows NT 10.0; Win64; x64; rv:77.0',
        ),
    ),
    models.DeviceInfo \
    (
        type    = enums.DeviceType.ANDROID,
        name    = 'Android',
        package = 'com.google.android',
        product = models.ProductInfo \
        (
            token = 'Linux; U; Android 9; en_GB; VirtualBox Build/PI',
        ),
    ),
    models.DeviceInfo \
    (
        type    = enums.DeviceType.IOS,
        name    = 'IOS',
        package = 'com.google.ios',
        product = models.ProductInfo \
        (
            token = 'iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB',
        ),
    ),
    models.DeviceInfo \
    (
        type    = enums.DeviceType.TV,
        name    = 'TV',
        product = models.ProductInfo \
        (
            name    = 'Mozilla',
            version = '5.0',
            token   = 'PlayStation; PlayStation 4/8.03',
        ),
    ),
)

services = Container \
(
    models.ServiceInfo \
    (
        type   = enums.ServiceType.YOUTUBE,
        name   = 'YouTube',
        domain = 'www.youtube.com',
        id     = 1,
    ),
    models.ServiceInfo \
    (
        type   = enums.ServiceType.YOUTUBE_MUSIC,
        name   = 'YouTube Music',
        domain = 'music.youtube.com',
        id     = 67,
    ),
    models.ServiceInfo \
    (
        type   = enums.ServiceType.YOUTUBE_KIDS,
        name   = 'YouTube Kids',
        domain = 'www.youtubekids.com',
        id     = 76,
    ),
    models.ServiceInfo \
    (
        type   = enums.ServiceType.YOUTUBE_STUDIO,
        name   = 'YouTube Studio',
        domain = 'studio.youtube.com',
        id     = 62,
    ),
)

apps = Container \
(
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_WEB,
        client  = clients.get(type = enums.ClientType.WEB),
        device  = devices.get(type = enums.DeviceType.WEB),
        service = services.get(type = enums.ServiceType.YOUTUBE),
        api     = models.ApiInfo(key = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_MUSIC_WEB,
        client  = clients.get(type = enums.ClientType.WEB_MUSIC),
        device  = devices.get(type = enums.DeviceType.WEB),
        service = services.get(type = enums.ServiceType.YOUTUBE_MUSIC),
        api     = models.ApiInfo(key = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30'),
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_KIDS_WEB,
        client  = clients.get(type = enums.ClientType.WEB_KIDS),
        device  = devices.get(type = enums.DeviceType.WEB),
        service = services.get(type = enums.ServiceType.YOUTUBE_KIDS),
        api     = models.ApiInfo(key = 'AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU'),
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_STUDIO_WEB,
        client  = clients.get(type = enums.ClientType.WEB_STUDIO),
        device  = devices.get(type = enums.DeviceType.WEB),
        service = services.get(type = enums.ServiceType.YOUTUBE_STUDIO),
        api     = models.ApiInfo(key = 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo'),
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_ANDROID,
        client  = clients.get(type = enums.ClientType.ANDROID),
        device  = devices.get(type = enums.DeviceType.ANDROID),
        service = services.get(type = enums.ServiceType.YOUTUBE),
        api     = models.ApiInfo(key = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w'),
        project = 'youtube',
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_MUSIC_ANDROID,
        client  = clients.get(type = enums.ClientType.ANDROID_MUSIC),
        device  = devices.get(type = enums.DeviceType.ANDROID),
        service = services.get(type = enums.ServiceType.YOUTUBE_MUSIC),
        api     = models.ApiInfo(key = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI'),
        project = 'apps.youtube.music',
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_KIDS_ANDROID,
        client  = clients.get(type = enums.ClientType.ANDROID_KIDS),
        device  = devices.get(type = enums.DeviceType.ANDROID),
        service = services.get(type = enums.ServiceType.YOUTUBE_KIDS),
        api     = models.ApiInfo(key = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk'),
        project = 'apps.youtube.kids',
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_STUDIO_ANDROID,
        client  = clients.get(type = enums.ClientType.ANDROID_STUDIO),
        device  = devices.get(type = enums.DeviceType.ANDROID),
        service = services.get(type = enums.ServiceType.YOUTUBE_STUDIO),
        api     = models.ApiInfo(key = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8'),
        project = 'apps.youtube.creator',
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_IOS,
        client  = clients.get(type = enums.ClientType.IOS),
        device  = devices.get(type = enums.DeviceType.IOS),
        service = services.get(type = enums.ServiceType.YOUTUBE),
        api     = models.ApiInfo(key = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc'),
        project = 'youtube',
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_MUSIC_IOS,
        client  = clients.get(type = enums.ClientType.IOS_MUSIC),
        device  = devices.get(type = enums.DeviceType.IOS),
        service = services.get(type = enums.ServiceType.YOUTUBE_MUSIC),
        api     = models.ApiInfo(key = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s'),
        project = 'youtubemusic',
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_KIDS_IOS,
        client  = clients.get(type = enums.ClientType.IOS_KIDS),
        device  = devices.get(type = enums.DeviceType.IOS),
        service = services.get(type = enums.ServiceType.YOUTUBE_KIDS),
        api     = models.ApiInfo(key = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc'),
        project = 'youtubekids',
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_STUDIO_IOS,
        client  = clients.get(type = enums.ClientType.IOS_STUDIO),
        device  = devices.get(type = enums.DeviceType.IOS),
        service = services.get(type = enums.ServiceType.YOUTUBE_STUDIO),
        api     = models.ApiInfo(key = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs'),
        project = 'ytcreator',
    ),
    models.AppInfo \
    (
        type    = enums.AppType.YOUTUBE_TV,
        client  = clients.get(type = enums.ClientType.TV),
        device  = devices.get(type = enums.DeviceType.TV),
        service = services.get(type = enums.ServiceType.YOUTUBE),
        api     = models.ApiInfo(key = 'AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8'),
    ),
)
