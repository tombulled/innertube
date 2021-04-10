import typing

from . import enums
from . import models

companies: typing.Dict[enums.Company, models.Company] = \
{
    enums.Company.GOOGLE: models.Company \
    (
        name   = 'Google',
        domain = 'google.com',
    )
}

products: typing.Dict[enums.Product, models.ProductIdentifier] = \
{
    enums.Product.MOZILLA: models.ProductIdentifier \
    (
        name    = 'Mozilla',
        version = '5.0',
    )
}

hosts: typing.Dict[enums.Host, models.Host] = \
{
    enums.Host.YOUTUBEI: models.Host \
    (
        domain = 'youtubei.googleapis.com',
    ),
    enums.Host.SUGGEST_QUERIES: models.Host \
    (
        domain = 'suggestqueries.google.com',
    ),
}

apis: typing.Dict[enums.Api, models.Api] = \
{
    enums.Api.YOUTUBEI_V1: models.Api \
    (
        host    = hosts[enums.Host.YOUTUBEI],
        mount   = 'youtubei/v1',
        version = 1,
    ),
    enums.Api.SUGGEST_QUERIES: models.Api \
    (
        host = hosts[enums.Host.SUGGEST_QUERIES],
    ),
}

devices: typing.Dict[enums.Device, models.Device] = \
{
    enums.Device.WEB: models.Device \
    (
        name    = 'Web',
        product = models.Device.Product \
        (
            identifier = products[enums.Product.MOZILLA],
            comment    = models.ProductComment \
            (
                comments = \
                (
                    'Windows NT 10.0',
                    'Win64',
                    'x64',
                    'rv:77.0',
                ),
            ),
        ),
    ),
    enums.Device.ANDROID: models.Device \
    (
        name    = 'Android',
        module  = 'com.google.android',
        product = models.Device.Product \
        (
            comment = models.ProductComment \
            (
                comments = \
                (
                    'Linux',
                    'U',
                    'Android 9',
                    'en_GB',
                    'VirtualBox Build/PI',
                ),
            ),
        ),
    ),
    enums.Device.IOS: models.Device \
    (
        name    = 'IOS',
        module  = 'com.google.ios',
        product = models.Device.Product \
        (
            comment = models.ProductComment \
            (
                comments = \
                (
                    'iPhone10,5',
                    'U',
                    'CPU iOS 14_4 like Mac OS X',
                    'en_GB',
                ),
            ),
        ),
    ),
    enums.Device.TV: models.Device \
    (
        name    = 'TV',
        product = models.Device.Product \
        (
            identifier = products[enums.Product.MOZILLA],
            comment    = models.ProductComment \
            (
                comments = \
                (
                    'PlayStation',
                    'PlayStation 4/8.03',
                ),
            ),
        ),
    ),
}

services: typing.Dict[enums.Service, models.Service] = \
{
    enums.Service.YOUTUBE: models.Service \
    (
        name   = 'YouTube',
        domain = 'www.youtube.com',
        id     = 1,
    ),
    enums.Service.YOUTUBE_MUSIC: models.Service \
    (
        name   = 'YouTube Music',
        domain = 'music.youtube.com',
        id     = 67,
    ),
    enums.Service.YOUTUBE_KIDS: models.Service \
    (
        name   = 'YouTube Kids',
        domain = 'www.youtubekids.com',
        id     = 76,
    ),
    enums.Service.YOUTUBE_STUDIO: models.Service \
    (
        name   = 'YouTube Studio',
        domain = 'studio.youtube.com',
        id     = 62,
    ),
}

clients: typing.Dict[enums.Client, models.Client] = \
{
    enums.Client.WEB: models.Client \
    (
        name       = 'WEB',
        version    = '2.20210223.09.00',
        identifier = 'youtube',
        auth       = models.Authentication \
        (
            api_key = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        ),
    ),
    enums.Client.WEB_MUSIC: models.Client \
    (
        name    = 'WEB_REMIX',
        version = '0.1',
        auth    = models.Authentication \
        (
            api_key = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30',
        ),
    ),
    enums.Client.WEB_KIDS: models.Client \
    (
        name       = 'WEB_KIDS',
        version    = '2.1.3',
        identifier = 'youtube-pegasus-web',
        auth    = models.Authentication \
        (
            api_key = 'AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU',
        ),
    ),
    enums.Client.WEB_STUDIO: models.Client \
    (
        name    = 'WEB_CREATOR',
        version = '1.20210223.01.00',
        auth    = models.Authentication \
        (
            api_key = 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo',
        ),
    ),
    enums.Client.ANDROID: models.Client \
    (
        name    = 'ANDROID',
        version = '16.07.34',
        module  = 'youtube',
        auth    = models.Authentication\
        (
            api_key = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w',
        ),
    ),
    enums.Client.ANDROID_MUSIC: models.Client \
    (
        name       = 'ANDROID_MUSIC',
        version    = '4.16.51',
        identifier = 'youtube-music-android',
        module     = 'apps.youtube.music',
        auth       = models.Authentication \
        (
            api_key = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI',
        ),
    ),
    enums.Client.ANDROID_KIDS: models.Client \
    (
        name    = 'ANDROID_KIDS',
        version = '6.02.3',
        module  = 'apps.youtube.kids',
        auth    = models.Authentication \
        (
            api_key = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk',
        ),
    ),
    enums.Client.ANDROID_STUDIO: models.Client \
    (
        name    = 'ANDROID_CREATOR',
        version = '21.06.103',
        module  = 'apps.youtube.creator',
        auth    = models.Authentication \
        (
            api_key = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8',
        ),
    ),
    enums.Client.IOS: models.Client \
    (
        name    = 'IOS',
        version = '16.05.7',
        module  = 'youtube',
        auth    = models.Authentication \
        (
            api_key = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
        ),
    ),
    enums.Client.IOS_MUSIC: models.Client \
    (
        name       = 'IOS_MUSIC',
        version    = '4.16.1',
        identifier = 'youtube-music-ios',
        module     = 'youtubemusic',
        auth       = models.Authentication \
        (
            api_key = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s',
        ),
    ),
    enums.Client.IOS_KIDS: models.Client \
    (
        name    = 'IOS_KIDS',
        version = '5.42.2',
        module  = 'youtubekids',
        auth    = models.Authentication \
        (
            api_key = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc',
        ),
    ),
    enums.Client.IOS_STUDIO: models.Client \
    (
        name    = 'IOS_CREATOR',
        version = '20.47.100',
        module  = 'ytcreator',
        auth    = models.Authentication \
        (
            api_key = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs',
        ),
    ),
    enums.Client.TV: models.Client \
    (
        name       = 'TVHTML5',
        version    = '7.20210224.00.00',
        identifier = 'youtube-lr',
        auth       = models.Authentication \
        (
            api_key = 'AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8',
        ),
    ),
}

schemas: typing.Dict[enums.App, models.AppSchema] = \
{
    enums.App.YOUTUBE_WEB: models.AppSchema \
    (
        client  = enums.Client.WEB,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE,
    ),
    enums.App.YOUTUBE_MUSIC_WEB: models.AppSchema \
    (
        client  = enums.Client.WEB_MUSIC,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    enums.App.YOUTUBE_KIDS_WEB: models.AppSchema \
    (
        client  = enums.Client.WEB_KIDS,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    enums.App.YOUTUBE_STUDIO_WEB: models.AppSchema \
    (
        client  = enums.Client.WEB_STUDIO,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    enums.App.YOUTUBE_ANDROID: models.AppSchema \
    (
        client  = enums.Client.ANDROID,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE,
    ),
    enums.App.YOUTUBE_MUSIC_ANDROID: models.AppSchema \
    (
        client  = enums.Client.ANDROID_MUSIC,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    enums.App.YOUTUBE_KIDS_ANDROID: models.AppSchema \
    (
        client  = enums.Client.ANDROID_KIDS,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    enums.App.YOUTUBE_STUDIO_ANDROID: models.AppSchema \
    (
        client  = enums.Client.ANDROID_STUDIO,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    enums.App.YOUTUBE_IOS: models.AppSchema \
    (
        client  = enums.Client.IOS,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE,
    ),
    enums.App.YOUTUBE_MUSIC_IOS: models.AppSchema \
    (
        client  = enums.Client.IOS_MUSIC,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    enums.App.YOUTUBE_KIDS_IOS: models.AppSchema \
    (
        client  = enums.Client.IOS_KIDS,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    enums.App.YOUTUBE_STUDIO_IOS: models.AppSchema \
    (
        client  = enums.Client.IOS_STUDIO,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    enums.App.YOUTUBE_TV: models.AppSchema \
    (
        client  = enums.Client.TV,
        device  = enums.Device.TV,
        service = enums.Service.YOUTUBE,
    ),
}

apps: typing.Dict[enums.App, models.App] = \
{
    app: models.App \
    (
        company = companies[enums.Company.GOOGLE],
        api     = apis[enums.Api.YOUTUBEI_V1],
        client  = clients[schema.client],
        device  = devices[schema.device],
        service = services[schema.service],
    )
    for app, schema in schemas.items()
}
