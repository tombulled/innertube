import typing

from . import enums
from . import models

apis: typing.Dict[enums.Host, models.Api] = \
{
    enums.Host.YOUTUBEI: models.Api \
    (
        domain = enums.Host.YOUTUBEI,
        mount  = '/youtubei/v1/',
    ),
    enums.Host.SUGGEST_QUERIES: models.Api \
    (
        domain = enums.Host.SUGGEST_QUERIES,
    ),
}

devices: typing.Dict[enums.Device, models.DeviceInfo] = \
{
    enums.Device.WEB: models.DeviceInfo \
    (
        identifier = enums.Device.WEB,
        family     = enums.DeviceFamily.WEB,
        comments   = \
        (
            'Windows NT 10.0',
            'Win64',
            'x64',
            'rv:77.0',
        ),
    ),
    enums.Device.ANDROID: models.DeviceInfo \
    (
        identifier = enums.Device.ANDROID,
        family     = enums.DeviceFamily.MOBILE,
        comments   = \
        (
            'Linux',
            'U',
            'Android 9',
            'en_GB',
            'VirtualBox Build/PI',
        ),
    ),
    enums.Device.IOS: models.DeviceInfo \
    (
        identifier = enums.Device.IOS,
        family     = enums.DeviceFamily.MOBILE,
        comments   = \
        (
            'iPhone10,5',
            'U',
            'CPU iOS 14_4 like Mac OS X',
            'en_GB',
        ),
    ),
    enums.Device.LR: models.DeviceInfo \
    (
        identifier = enums.Device.LR,
        family     = enums.DeviceFamily.WEB,
        comments   = \
        (
            'PlayStation',
            'PlayStation 4/8.03',
        ),
    ),
}

services: typing.Dict[enums.Service, models.ServiceInfo] = \
{
    enums.Service.YOUTUBE: models.ServiceInfo \
    (
        domain = enums.Host.YOUTUBE,
    ),
    enums.Service.YOUTUBE_MUSIC: models.ServiceInfo \
    (
        domain = enums.Host.YOUTUBE_MUSIC,
    ),
    enums.Service.YOUTUBE_KIDS: models.ServiceInfo \
    (
        domain = enums.Host.YOUTUBE_KIDS,
    ),
    enums.Service.YOUTUBE_STUDIO: models.ServiceInfo \
    (
        domain = enums.Host.YOUTUBE_STUDIO,
    ),
}

clients: typing.Dict[enums.Client, models.ClientInfo] = \
{
    enums.Client.WEB: models.ClientInfo \
    (
        name    = enums.Client.WEB,
        version = '2.20210223.09.00',
        key     = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        client  = enums.FrontEnd.YOUTUBE,
        id      = enums.ClientId.WEB,
    ),
    enums.Client.WEB_REMIX: models.ClientInfo \
    (
        name    = enums.Client.WEB_REMIX,
        version = '0.1',
        key     = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30',
        id      = enums.ClientId.WEB_REMIX,
    ),
    enums.Client.WEB_KIDS: models.ClientInfo \
    (
        name    = enums.Client.WEB_KIDS,
        version = '2.1.4',
        key     = 'AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU',
        client  = enums.FrontEnd.YOUTUBE_PEGASUS_WEB,
        id      = enums.ClientId.WEB_KIDS,
    ),
    enums.Client.WEB_CREATOR: models.ClientInfo \
    (
        name    = enums.Client.WEB_CREATOR,
        version = '1.20210223.01.00',
        key     = 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo',
        id      = enums.ClientId.WEB_CREATOR,
    ),
    enums.Client.ANDROID: models.ClientInfo \
    (
        name    = enums.Client.ANDROID,
        version = '16.07.34',
        key     = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w',
        project = 'youtube',
    ),
    enums.Client.ANDROID_MUSIC: models.ClientInfo \
    (
        name    = enums.Client.ANDROID_MUSIC,
        version = '4.16.51',
        key     = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI',
        project = 'apps.youtube.music',
        client  = enums.FrontEnd.YOUTUBE_MUSIC_ANDROID,
    ),
    enums.Client.ANDROID_KIDS: models.ClientInfo \
    (
        name    = enums.Client.ANDROID_KIDS,
        version = '6.02.3',
        key     = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk',
        project = 'apps.youtube.kids',
    ),
    enums.Client.ANDROID_CREATOR: models.ClientInfo \
    (
        name    = enums.Client.ANDROID_CREATOR,
        version = '21.06.103',
        key     = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8',
        project = 'apps.youtube.creator',
    ),
    enums.Client.IOS: models.ClientInfo \
    (
        name    = enums.Client.IOS,
        version = '16.05.7',
        key     = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
        project = 'youtube',
    ),
    enums.Client.IOS_MUSIC: models.ClientInfo \
    (
        name    = enums.Client.IOS_MUSIC,
        version = '4.16.1',
        key     = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s',
        project = 'youtubemusic',
        client  = enums.FrontEnd.YOUTUBE_MUSIC_IOS,
    ),
    enums.Client.IOS_KIDS: models.ClientInfo \
    (
        name    = enums.Client.IOS_KIDS,
        version = '5.42.2',
        key     = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc',
        project = 'youtubekids',
    ),
    enums.Client.IOS_CREATOR: models.ClientInfo \
    (
        name    = enums.Client.IOS_CREATOR,
        version = '20.47.100',
        key     = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs',
        project = 'ytcreator',
    ),
    enums.Client.TVHTML5: models.ClientInfo \
    (
        name    = enums.Client.TVHTML5,
        version = '7.20210224.00.00',
        key     = 'AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8',
        client  = enums.FrontEnd.YOUTUBE_LR,
    ),
}

schemas: typing.Tuple[models.ClientSchema] = \
(
    models.ClientSchema \
    (
        client  = enums.Client.WEB,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.WEB_REMIX,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.WEB_KIDS,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.WEB_CREATOR,
        device  = enums.Device.WEB,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.ANDROID,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.ANDROID_MUSIC,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.ANDROID_KIDS,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.ANDROID_CREATOR,
        device  = enums.Device.ANDROID,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.IOS,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.IOS_MUSIC,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_MUSIC,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.IOS_KIDS,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_KIDS,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.IOS_CREATOR,
        device  = enums.Device.IOS,
        service = enums.Service.YOUTUBE_STUDIO,
    ),
    models.ClientSchema \
    (
        client  = enums.Client.TVHTML5,
        device  = enums.Device.LR,
        service = enums.Service.YOUTUBE,
    ),
)

clients = \
{
    schema.client: models.Client \
    (
        client  = clients[schema.client],
        device  = devices[schema.device],
        service = services[schema.service],
    )
    for schema in schemas
}
