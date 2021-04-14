import typing

import useragent

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

products: typing.Dict[enums.Product, useragent.ProductIdentifier] = \
{
    enums.Product.MOZILLA: useragent.ProductIdentifier \
    (
        name    = 'Mozilla',
        version = '5.0',
    )
}

apis: typing.Dict[enums.Api, models.Host] = \
{
    enums.Api.YOUTUBEI: models.Host \
    (
        domain = 'youtubei.googleapis.com',
        path   = '/youtubei/v1/',
    ),
    enums.Api.SUGGEST_QUERIES: models.Host \
    (
        domain = 'suggestqueries.google.com',
    ),
}

devices: typing.Dict[enums.Device, models.Device] = \
{
    enums.Device.WEB: models.Device \
    (
        name       = 'Web',
        identifier = 'web',
        comments   = \
        (
            'Windows NT 10.0',
            'Win64',
            'x64',
            'rv:77.0',
        ),
        product = products[enums.Product.MOZILLA],
    ),
    enums.Device.ANDROID: models.Device \
    (
        name       = 'Android',
        identifier = 'android',
        comments   = \
        (
            'Linux',
            'U',
            'Android 9',
            'en_GB',
            'VirtualBox Build/PI',
        ),
    ),
    enums.Device.IOS: models.Device \
    (
        name       = 'IOS',
        identifier = 'ios',
        comments   = \
        (
            'iPhone10,5',
            'U',
            'CPU iOS 14_4 like Mac OS X',
            'en_GB',
        ),
    ),
    enums.Device.TV: models.Device \
    (
        name       = 'TV',
        identifier = 'lr',
        comments   = \
        (
            'PlayStation',
            'PlayStation 4/8.03',
        ),
        product = products[enums.Product.MOZILLA],
    ),
}

services: typing.Dict[enums.Service, models.Service] = \
{
    enums.Service.YOUTUBE: models.Service \
    (
        name       = 'YouTube',
        identifier = 'youtube',
        domain     = 'www.youtube.com',
        id         = 1,
    ),
    enums.Service.YOUTUBE_MUSIC: models.Service \
    (
        name       = 'YouTube Music',
        identifier = 'youtube-music',
        domain     = 'music.youtube.com',
        id         = 67,
    ),
    enums.Service.YOUTUBE_KIDS: models.Service \
    (
        name       = 'YouTube Kids',
        identifier = 'youtube-pegasus',
        domain     = 'www.youtubekids.com',
        id         = 76,
    ),
    enums.Service.YOUTUBE_STUDIO: models.Service \
    (
        name       = 'YouTube Studio',
        identifier = 'youtube-creator',
        domain     = 'studio.youtube.com',
        id         = 62,
    ),
}

clients: typing.Dict[enums.Client, models.Client] = \
{
    enums.Client.WEB: models.Client \
    (
        name       = 'WEB',
        version    = '2.20210223.09.00',
        identifier = 'youtube',
        key        = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
    ),
    enums.Client.WEB_REMIX: models.Client \
    (
        name    = 'WEB_REMIX',
        version = '0.1',
        key     = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30',
    ),
    enums.Client.WEB_KIDS: models.Client \
    (
        name       = 'WEB_KIDS',
        version    = '2.1.3',
        key        = 'AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU',
        identifier = 'youtube-pegasus-web',
    ),
    enums.Client.WEB_CREATOR: models.Client \
    (
        name    = 'WEB_CREATOR',
        version = '1.20210223.01.00',
        key     = 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo',
    ),
    enums.Client.ANDROID: models.Client \
    (
        name    = 'ANDROID',
        version = '16.07.34',
        package = 'youtube',
        key     = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w',
    ),
    enums.Client.ANDROID_MUSIC: models.Client \
    (
        name       = 'ANDROID_MUSIC',
        version    = '4.16.51',
        identifier = 'youtube-music-android',
        package    = 'apps.youtube.music',
        key        = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI',
    ),
    enums.Client.ANDROID_KIDS: models.Client \
    (
        name    = 'ANDROID_KIDS',
        version = '6.02.3',
        package = 'apps.youtube.kids',
        key     = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk',
    ),
    enums.Client.ANDROID_CREATOR: models.Client \
    (
        name    = 'ANDROID_CREATOR',
        version = '21.06.103',
        package = 'apps.youtube.creator',
        key     = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8',
    ),
    enums.Client.IOS: models.Client \
    (
        name    = 'IOS',
        version = '16.05.7',
        package = 'youtube',
        key     = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
    ),
    enums.Client.IOS_MUSIC: models.Client \
    (
        name       = 'IOS_MUSIC',
        version    = '4.16.1',
        identifier = 'youtube-music-ios',
        package    = 'youtubemusic',
        key        = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s',
    ),
    enums.Client.IOS_KIDS: models.Client \
    (
        name    = 'IOS_KIDS',
        version = '5.42.2',
        package = 'youtubekids',
        key     = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc',
    ),
    enums.Client.IOS_CREATOR: models.Client \
    (
        name    = 'IOS_CREATOR',
        version = '20.47.100',
        package = 'ytcreator',
        key     = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs',
    ),
    enums.Client.TVHTML5: models.Client \
    (
        name       = 'TVHTML5',
        version    = '7.20210224.00.00',
        identifier = 'youtube-lr',
        key        = 'AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8',
    ),
}

schemas: typing.Dict[enums.Client, models.ClientSchema] = \
{
    enums.Client.WEB: models.ClientSchema \
    (
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE,
    ),
    enums.Client.WEB_REMIX: models.ClientSchema \
    (
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    enums.Client.WEB_KIDS: models.ClientSchema \
    (
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    enums.Client.WEB_CREATOR: models.ClientSchema \
    (
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    enums.Client.ANDROID: models.ClientSchema \
    (
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE,
    ),
    enums.Client.ANDROID_MUSIC: models.ClientSchema \
    (
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    enums.Client.ANDROID_KIDS: models.ClientSchema \
    (
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    enums.Client.ANDROID_CREATOR: models.ClientSchema \
    (
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    enums.Client.IOS: models.ClientSchema \
    (
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE,
    ),
    enums.Client.IOS_MUSIC: models.ClientSchema \
    (
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    enums.Client.IOS_KIDS: models.ClientSchema \
    (
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    enums.Client.IOS_CREATOR: models.ClientSchema \
    (
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    enums.Client.TVHTML5: models.ClientSchema \
    (
        device  = enums.Device.TV,
        service = enums.Service.YOUTUBE,
    ),
}
