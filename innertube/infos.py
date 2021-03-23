import enum
import pydantic

from . import models
from . import enums

from typing import \
(
    List,
    Optional
)

class ModelContainer(enum.Enum):
    @classmethod
    def search(cls, **kwargs) -> List[pydantic.BaseModel]:
        return \
        [
            member.value
            for member in cls.__members__.values()
            for field_name, field_value in kwargs.items()
            if (value := getattr(member.value, field_name, None)) and value == field_value
        ]

    @classmethod
    def get(cls, **kwargs) -> Optional[pydantic.BaseModel]:
        if (results := cls.search(**kwargs)):
            return results[0]

class Clients(ModelContainer):
    Web = models.ClientInfo \
    (
        type       = enums.ClientType.WEB,
        name       = 'WEB',
        version    = '2.20210223.09.00',
        identifier = 'youtube',
    )

    WebMusic = models.ClientInfo \
    (
        type    = enums.ClientType.WEB_MUSIC,
        name    = 'WEB_REMIX',
        version = '0.1',
    )

    WebKids = models.ClientInfo \
    (
        type       = enums.ClientType.WEB_KIDS,
        name       = 'WEB_KIDS',
        version    = '2.1.3',
        identifier = 'youtube-pegasus-web',
    )

    WebStudio = models.ClientInfo \
    (
        type    = enums.ClientType.WEB_STUDIO,
        name    = 'WEB_CREATOR',
        version = '1.20210223.01.00',
    )

    Android = models.ClientInfo \
    (
        type    = enums.ClientType.ANDROID,
        name    = 'ANDROID',
        version = '16.07.34',
    )

    AndroidMusic = models.ClientInfo \
    (
        type       = enums.ClientType.ANDROID_MUSIC,
        name       = 'ANDROID_MUSIC',
        version    = '4.16.51',
        identifier = 'youtube-music-android',
    )

    AndroidKids = models.ClientInfo \
    (
        type    = enums.ClientType.ANDROID_KIDS,
        name    = 'ANDROID_KIDS',
        version = '6.02.3',
    )

    AndroidStudio = models.ClientInfo \
    (
        type    = enums.ClientType.ANDROID_STUDIO,
        name    = 'ANDROID_CREATOR',
        version = '21.06.103',
    )

    Ios = models.ClientInfo \
    (
        type    = enums.ClientType.IOS,
        name    = 'IOS',
        version = '16.05.7',
    )

    IosMusic = models.ClientInfo \
    (
        type       = enums.ClientType.IOS_MUSIC,
        name       = 'IOS_MUSIC',
        version    = '4.16.1',
        identifier = 'youtube-music-ios',
    )

    IosKids = models.ClientInfo \
    (
        type    = enums.ClientType.IOS_KIDS,
        name    = 'IOS_KIDS',
        version = '5.42.2',
    )

    IosStudio = models.ClientInfo \
    (
        type    = enums.ClientType.IOS_STUDIO,
        name    = 'IOS_CREATOR',
        version = '20.47.100',
    )

    Tv = models.ClientInfo \
    (
        type       = enums.ClientType.TV,
        name       = 'TVHTML5',
        version    = '7.20210224.00.00',
        identifier = 'youtube-lr',
    )

class Devices(ModelContainer):
    Web = models.DeviceInfo \
    (
        type    = enums.DeviceType.WEB,
        name    = 'Web',
        product = models.ProductInfo \
        (
            name    = 'Mozilla',
            version = '5.0',
            token   = 'Windows NT 10.0; Win64; x64; rv:77.0',
        ),
    )

    Android = models.DeviceInfo \
    (
        type    = enums.DeviceType.ANDROID,
        name    = 'Android',
        package = 'com.google.android',
        product = models.ProductInfo \
        (
            token = 'Linux; U; Android 9; en_GB; VirtualBox Build/PI',
        ),
    )

    Ios = models.DeviceInfo \
    (
        type    = enums.DeviceType.IOS,
        name    = 'IOS',
        package = 'com.google.ios',
        product = models.ProductInfo \
        (
            token = 'iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB',
        ),
    )

    Tv = models.DeviceInfo \
    (
        type    = enums.DeviceType.TV,
        name    = 'TV',
        product = models.ProductInfo \
        (
            name    = 'Mozilla',
            version = '5.0',
            token   = 'PlayStation; PlayStation 4/8.03',
        ),
    )

class Services(ModelContainer):
    YouTube = models.ServiceInfo \
    (
        type      = enums.ServiceType.YOUTUBE,
        name      = 'YouTube',
        domain    = 'www.youtube.com',
        id        = 1,
        endpoints = \
        [
            enums.Endpoint.CONFIG,
            enums.Endpoint.BROWSE,
            enums.Endpoint.PLAYER,
            enums.Endpoint.GUIDE,
            enums.Endpoint.SEARCH,
            enums.Endpoint.NEXT,
        ],
    )

    YOUTUBE_MUSIC = models.ServiceInfo \
    (
        type      = enums.ServiceType.YOUTUBE_MUSIC,
        name      = 'YouTube Music',
        domain    = 'music.youtube.com',
        id        = 67,
        endpoints = \
        [
            enums.Endpoint.CONFIG,
            enums.Endpoint.BROWSE,
            enums.Endpoint.PLAYER,
            enums.Endpoint.GUIDE,
            enums.Endpoint.SEARCH,
            enums.Endpoint.NEXT,
            enums.Endpoint.MUSIC_GET_SEARCH_SUGGESTIONS,
            enums.Endpoint.MUSIC_GET_QUEUE,
        ],
    )

    YouTubeKids = models.ServiceInfo \
    (
        type      = enums.ServiceType.YOUTUBE_KIDS,
        name      = 'YouTube Kids',
        domain    = 'www.youtubekids.com',
        id        = 76,
        endpoints = \
        [
            enums.Endpoint.CONFIG,
            enums.Endpoint.BROWSE,
            enums.Endpoint.PLAYER,
            enums.Endpoint.SEARCH,
            enums.Endpoint.NEXT,
        ],
    )

    YouTubeStudio = models.ServiceInfo \
    (
        type      = enums.ServiceType.YOUTUBE_STUDIO,
        name      = 'YouTube Studio',
        domain    = 'studio.youtube.com',
        id        = 62,
        endpoints = \
        [
            enums.Endpoint.CONFIG,
            enums.Endpoint.BROWSE,
            enums.Endpoint.PLAYER,
        ],
    )

class Apps(ModelContainer):
    YouTubeWeb = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.WEB),
        device  = Devices.get(type = enums.DeviceType.WEB),
        service = Services.get(type = enums.ServiceType.YOUTUBE),
        api     = models.ApiInfo(key = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
    )

    YouTubeMusicWeb = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.WEB_MUSIC),
        device  = Devices.get(type = enums.DeviceType.WEB),
        service = Services.get(type = enums.ServiceType.YOUTUBE_MUSIC),
        api     = models.ApiInfo(key = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30'),
    )

    YouTubeKidsWeb = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.WEB_KIDS),
        device  = Devices.get(type = enums.DeviceType.WEB),
        service = Services.get(type = enums.ServiceType.YOUTUBE_KIDS),
        api     = models.ApiInfo(key = 'AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU'),
    )

    YouTubeStudioWeb = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.WEB_STUDIO),
        device  = Devices.get(type = enums.DeviceType.WEB),
        service = Services.get(type = enums.ServiceType.YOUTUBE_STUDIO),
        api     = models.ApiInfo(key = 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo'),
    )

    YouTubeAndroid = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.ANDROID),
        device  = Devices.get(type = enums.DeviceType.ANDROID),
        service = Services.get(type = enums.ServiceType.YOUTUBE),
        api     = models.ApiInfo(key = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w'),
        project = 'youtube',
    )

    YouTubeMusicAndroid = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.ANDROID_MUSIC),
        device  = Devices.get(type = enums.DeviceType.ANDROID),
        service = Services.get(type = enums.ServiceType.YOUTUBE_MUSIC),
        api     = models.ApiInfo(key = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI'),
        project = 'apps.youtube.music',
    )

    YouTubeKidsAndroid = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.ANDROID_KIDS),
        device  = Devices.get(type = enums.DeviceType.ANDROID),
        service = Services.get(type = enums.ServiceType.YOUTUBE_KIDS),
        api     = models.ApiInfo(key = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk'),
        project = 'apps.youtube.kids',
    )

    YouTubeStudioAndroid = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.ANDROID_STUDIO),
        device  = Devices.get(type = enums.DeviceType.ANDROID),
        service = Services.get(type = enums.ServiceType.YOUTUBE_STUDIO),
        api     = models.ApiInfo(key = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8'),
        project = 'apps.youtube.creator',
    )

    YouTubeIos = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.IOS),
        device  = Devices.get(type = enums.DeviceType.IOS),
        service = Services.get(type = enums.ServiceType.YOUTUBE),
        api     = models.ApiInfo(key = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc'),
        project = 'youtube',
    )

    YouTubeMusicIos = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.IOS_MUSIC),
        device  = Devices.get(type = enums.DeviceType.IOS),
        service = Services.get(type = enums.ServiceType.YOUTUBE_MUSIC),
        api     = models.ApiInfo(key = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s'),
        project = 'youtubemusic',
    )

    YouTubeKidsIos = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.IOS_KIDS),
        device  = Devices.get(type = enums.DeviceType.IOS),
        service = Services.get(type = enums.ServiceType.YOUTUBE_KIDS),
        api     = models.ApiInfo(key = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc'),
        project = 'youtubekids',
    )

    YouTubeStudioIos = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.IOS_STUDIO),
        device  = Devices.get(type = enums.DeviceType.IOS),
        service = Services.get(type = enums.ServiceType.YOUTUBE_STUDIO),
        api     = models.ApiInfo(key = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs'),
        project = 'ytcreator',
    )

    YouTubeTv = models.AppInfo \
    (
        client  = Clients.get(type = enums.ClientType.TV),
        device  = Devices.get(type = enums.DeviceType.TV),
        service = Services.get(type = enums.ServiceType.YOUTUBE),
        api     = models.ApiInfo(key = 'AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8'),
    )
