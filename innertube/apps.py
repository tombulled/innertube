from . import models
from . import clients
from . import devices
from . import services

YouTubeWeb = models.AppInfo \
(
    client  = clients.Web,
    device  = devices.Web,
    service = services.YouTube,
    api     = models.ApiInfo(key = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8'),
)

YouTubeMusicWeb = models.AppInfo \
(
    client  = clients.WebMusic,
    device  = devices.Web,
    service = services.YouTubeMusic,
    api     = models.ApiInfo(key = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30'),
)

YouTubeKidsWeb = models.AppInfo \
(
    client  = clients.WebKids,
    device  = devices.Web,
    service = services.YouTubeKids,
    api     = models.ApiInfo(key = 'AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU'),
)

YouTubeStudioWeb = models.AppInfo \
(
    client  = clients.WebStudio,
    device  = devices.Web,
    service = services.YouTubeStudio,
    api     = models.ApiInfo(key = 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo'),
)

YouTubeAndroid = models.AppInfo \
(
    client  = clients.Android,
    device  = devices.Android,
    service = services.YouTube,
    api     = models.ApiInfo(key = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w'),
    project = 'youtube',
)

YouTubeMusicAndroid = models.AppInfo \
(
    client  = clients.AndroidMusic,
    device  = devices.Android,
    service = services.YouTubeMusic,
    api     = models.ApiInfo(key = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI'),
    project = 'apps.youtube.music',
)

YouTubeKidsAndroid = models.AppInfo \
(
    client  = clients.AndroidKids,
    device  = devices.Android,
    service = services.YouTubeKids,
    api     = models.ApiInfo(key = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk'),
    project = 'apps.youtube.kids',
)

YouTubeStudioAndroid = models.AppInfo \
(
    client  = clients.AndroidStudio,
    device  = devices.Android,
    service = services.YouTubeStudio,
    api     = models.ApiInfo(key = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8'),
    project = 'apps.youtube.creator',
)

YouTubeIos = models.AppInfo \
(
    client  = clients.Ios,
    device  = devices.Ios,
    service = services.YouTube,
    api     = models.ApiInfo(key = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc'),
    project = 'youtube',
)

YouTubeMusicIos = models.AppInfo \
(
    client  = clients.IosMusic,
    device  = devices.Ios,
    service = services.YouTubeMusic,
    api     = models.ApiInfo(key = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s'),
    project = 'youtubemusic',
)

YouTubeKidsIos = models.AppInfo \
(
    client  = clients.IosKids,
    device  = devices.Ios,
    service = services.YouTubeKids,
    api     = models.ApiInfo(key = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc'),
    project = 'youtubekids',
)

YouTubeStudioIos = models.AppInfo \
(
    client  = clients.IosStudio,
    device  = devices.Ios,
    service = services.YouTubeStudio,
    api     = models.ApiInfo(key = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs'),
    project = 'ytcreator',
)

YouTubeTv = models.AppInfo \
(
    client  = clients.Tv,
    device  = devices.Tv,
    service = services.YouTube,
    api     = models.ApiInfo(key = 'AIzaSyDCU8hByM-4DrUqRUYnGn-3llEO78bcxq8'),
)
