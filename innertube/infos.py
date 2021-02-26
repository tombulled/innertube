from . import info
from . import services
from . import devices

Web = info.ClientInfo \
(
    name    = 'WEB',
    version = '2.20210223.09.00',
    device  = devices.Web,
    service = services.YouTube,
    api     = info.ApiInfo(key = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
)

WebMusic = info.ClientInfo \
(
    name    = 'WEB_REMIX',
    version = '0.1',
    device  = devices.Web,
    service = services.YouTubeMusic,
    api     = info.ApiInfo(key = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30'),
)

WebKids = info.ClientInfo \
(
    name    = 'WEB_KIDS',
    version = '2.1.3',
    device  = devices.Web,
    service = services.YouTubeKids,
    api     = info.ApiInfo(key = 'AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU'),
)

WebStudio = info.ClientInfo \
(
    name    = 'WEB_CREATOR',
    version = '1.20210223.01.00',
    device  = devices.Web,
    service = services.YouTubeStudio,
    api     = info.ApiInfo(key = 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo'),
)

Android = info.ClientInfo \
(
    name    = 'ANDROID',
    version = '16.07.34',
    device  = devices.Android,
    service = services.YouTube,
    api     = info.ApiInfo(key = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w'),
)

AndroidMusic = info.ClientInfo \
(
    name    = 'ANDROID_MUSIC',
    version = '4.16.51',
    device  = devices.Android,
    service = services.YouTubeMusic,
    api     = info.ApiInfo(key = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI'),
)

AndroidKids = info.ClientInfo \
(
    name    = 'ANDROID_KIDS',
    version = '6.02.3',
    device  = devices.Android,
    service = services.YouTubeKids,
    api     = info.ApiInfo(key = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk'),
)

AndroidStudio = info.ClientInfo \
(
    name    = 'ANDROID_CREATOR',
    version = '21.06.103',
    device  = devices.Android,
    service = services.YouTubeStudio,
    api     = info.ApiInfo(key = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8'),
)

Ios = info.ClientInfo \
(
    name    = 'IOS',
    version = '16.05.7',
    device  = devices.Ios,
    service = services.YouTube,
    api     = info.ApiInfo(key = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc'),
)

IosMusic = info.ClientInfo \
(
    name    = 'IOS_MUSIC',
    version = '4.16.1',
    device  = devices.Ios,
    service = services.YouTubeMusic,
    api     = info.ApiInfo(key = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s'),
)

IosKids = info.ClientInfo \
(
    name    = 'IOS_KIDS',
    version = '5.42.2',
    device  = devices.Ios,
    service = services.YouTubeKids,
    api     = info.ApiInfo(key = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc'),
)

IosStudio = info.ClientInfo \
(
    name    = 'IOS_CREATOR',
    version = '20.47.100',
    device  = devices.Ios,
    service = services.YouTubeStudio,
    api     = info.ApiInfo(key = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs'),
)
