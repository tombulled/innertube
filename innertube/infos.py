import typing

import useragent

from . import enums
from . import models

def client(service: enums.Service, device: enums.Device) -> typing.Optional[enums.Client]:
    for client, schema in schemas.items():
        if schema.service == service and schema.device == device:
            return client

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

hosts: typing.Dict[enums.Host, models.Host] = \
{
    enums.Host.YOUTUBEI: models.Host \
    (
        domain = 'youtubei.googleapis.com',
        path   = '/youtubei/v1/',
    ),
    enums.Host.SUGGEST_QUERIES: models.Host \
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
        name       = 'iOS',
        identifier = 'ios',
        comments   = \
        (
            'iPhone10,5',
            'U',
            'CPU iOS 14_4 like Mac OS X',
            'en_GB',
        ),
    ),
    enums.Device.LR: models.Device \
    (
        name       = 'LR',
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
        identifier = 'youtube-kids',
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
        key        = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        identifier = 'youtube',
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
        key     = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w',
        package = 'youtube',
    ),
    enums.Client.ANDROID_MUSIC: models.Client \
    (
        name       = 'ANDROID_MUSIC',
        version    = '4.16.51',
        key        = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI',
        identifier = 'youtube-music-android',
        package    = 'apps.youtube.music',
    ),
    enums.Client.ANDROID_KIDS: models.Client \
    (
        name    = 'ANDROID_KIDS',
        version = '6.02.3',
        key     = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk',
        package = 'apps.youtube.kids',
    ),
    enums.Client.ANDROID_CREATOR: models.Client \
    (
        name    = 'ANDROID_CREATOR',
        version = '21.06.103',
        key     = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8',
        package = 'apps.youtube.creator',
    ),
    enums.Client.IOS: models.Client \
    (
        name    = 'IOS',
        version = '16.05.7',
        key     = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
        package = 'youtube',
    ),
    enums.Client.IOS_MUSIC: models.Client \
    (
        name       = 'IOS_MUSIC',
        version    = '4.16.1',
        key        = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s',
        identifier = 'youtube-music-ios',
        package    = 'youtubemusic',
    ),
    enums.Client.IOS_KIDS: models.Client \
    (
        name    = 'IOS_KIDS',
        version = '5.42.2',
        key     = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc',
        package = 'youtubekids',
    ),
    enums.Client.IOS_CREATOR: models.Client \
    (
        name    = 'IOS_CREATOR',
        version = '20.47.100',
        key     = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs',
        package = 'ytcreator',
    ),
    enums.Client.TVHTML5: models.Client \
    (
        name       = 'TVHTML5',
        version    = '7.20210224.00.00',
        key        = 'AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8',
        identifier = 'youtube-lr',
    ),
}

schemas: typing.Tuple[models.Schema] = \
(
    models.Schema \
    (
        client  = enums.Client.WEB,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE,
    ),
    models.Schema \
    (
        client  = enums.Client.WEB_REMIX,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    models.Schema \
    (
        client  = enums.Client.WEB_KIDS,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    models.Schema \
    (
        client  = enums.Client.WEB_CREATOR,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    models.Schema \
    (
        client  = enums.Client.ANDROID,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE,
    ),
    models.Schema \
    (
        client  = enums.Client.ANDROID_MUSIC,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    models.Schema \
    (
        client  = enums.Client.ANDROID_KIDS,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    models.Schema \
    (
        client  = enums.Client.ANDROID_CREATOR,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    models.Schema \
    (
        client  = enums.Client.IOS,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE,
    ),
    models.Schema \
    (
        client  = enums.Client.IOS_MUSIC,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    models.Schema \
    (
        client  = enums.Client.IOS_KIDS,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    models.Schema \
    (
        client  = enums.Client.IOS_CREATOR,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    models.Schema \
    (
        client  = enums.Client.TVHTML5,
        device  = enums.Device.LR,
        service = enums.Service.YOUTUBE,
    ),
)
