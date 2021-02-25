from pydantic import BaseModel

class Client(BaseModel):
    name:    str
    version: str

class Api(BaseModel):
    key:     str
    domain:  str
    version: int

class Adaptor(BaseModel):
    user_agent: str
    origin:     str

class Service(BaseModel):
    client:  Client
    api:     Api
    adaptor: Adaptor

WEB = Service \
(
    client = Client \
    (
        name    = 'WEB',
        version = '2.20210223.09.00',
    ),
    api = Api \
    (
        key     = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        domain  = 'youtubei.googleapis.com', # Uses: www.youtube.com
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        origin     = 'www.youtube.com',
    ),
)

WEB_REMIX = Service \
(
    client = Client \
    (
        name    = 'WEB_REMIX',
        version = '0.1',
    ),
    api = Api \
    (
        key     = 'AIzaSyC9XL3ZjWddXya6X74dJoCTL-WEYFDNX30',
        domain  = 'youtubei.googleapis.com', # Uses: music.youtube.com
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        origin     = 'music.youtube.com',
    ),
)

WEB_KIDS = Service \
(
    client = Client \
    (
        name    = 'WEB_KIDS',
        version = '2.1.3',
    ),
    api = Api \
    (
        key     = 'AIzaSyBbZV_fZ3an51sF-mvs5w37OqqbsTOzwtU',
        domain  = 'youtubei.googleapis.com', # Uses: www.youtubekids.com
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        origin     = 'www.youtubekids.com',
    ),
)

WEB_CREATOR = Service \
(
    client = Client \
    (
        name    = 'WEB_CREATOR',
        version = '1.20210223.01.00',
    ),
    api = Api \
    (
        key     = 'AIzaSyBUPetSUmoZL-OhlxA7wSac5XinrygCqMo',
        domain  = 'youtubei.googleapis.com', # Uses: studio.youtube.com
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        origin     = 'studio.youtube.com',
    ),
)

IOS = Service \
(
    client = Client \
    (
        name    = 'IOS',
        version = '16.05.7',
    ),
    api = Api \
    (
        key     = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.ios.youtube/16.05.7 (iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB)',
        origin     = 'www.youtube.com',
    ),
)

IOS_MUSIC = Service \
(
    client = Client \
    (
        name    = 'IOS_MUSIC',
        version = '4.16.1',
    ),
    api = Api \
    (
        key     = 'AIzaSyBAETezhkwP0ZWA02RsqT1zu78Fpt0bC_s',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.ios.youtubemusic/4.16.1 (iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB)',
        origin     = 'music.youtube.com',
    ),
)

IOS_KIDS = Service \
(
    client = Client \
    (
        name    = 'IOS_KIDS',
        version = '5.42.2',
    ),
    api = Api \
    (
        key     = 'AIzaSyA6_JWXwHaVBQnoutCv1-GvV97-rJ949Bc',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.ios.youtubekids/5.42.2 (iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB)',
        origin     = 'www.youtubekids.com',
    ),
)

IOS_CREATOR = Service \
(
    client = Client \
    (
        name    = 'IOS_CREATOR',
        version = '20.47.100',
    ),
    api = Api \
    (
        key     = 'AIzaSyAPyF5GfQI-kOa6nZwO8EsNrGdEx9bioNs',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.ios.ytcreator/20.47.100 (iPhone10,5; U; CPU iOS 14_4 like Mac OS X; en_GB)',
        origin     = 'studio.youtube.com',
    ),
)

ANDROID = Service \
(
    client = Client \
    (
        name    = 'ANDROID',
        version = '16.07.34',
    ),
    api = Api \
    (
        key     = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.android.youtube/16.07.34(Linux; U; Android 9; en_GB; VirtualBox Build/PI)',
        origin     = 'www.youtube.com',
    ),
)

ANDROID_MUSIC = Service \
(
    client = Client \
    (
        name    = 'ANDROID_MUSIC',
        version = '4.16.51',
    ),
    api = Api \
    (
        key     = 'AIzaSyAOghZGza2MQSZkY_zfZ370N-PUdXEo8AI',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.android.apps.youtube.music/4.16.51(Linux; U; Android 9; en_GB; VirtualBox Build/PI)',
        origin     = 'music.youtube.com',
    ),
)

ANDROID_KIDS = Service \
(
    client = Client \
    (
        name    = 'ANDROID_KIDS',
        version = '6.02.3',
    ),
    api = Api \
    (
        key     = 'AIzaSyAxxQKWYcEX8jHlflLt2Qcbb-rlolzBhhk',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.android.apps.youtube.kids/6.02.3(Linux; U; Android 9; en_GB; VirtualBox Build/PI)',
        origin     = 'www.youtubekids.com',
    ),
)

ANDROID_CREATOR = Service \
(
    client = Client \
    (
        name    = 'ANDROID_CREATOR',
        version = '21.06.103',
    ),
    api = Api \
    (
        key     = 'AIzaSyD_qjV8zaaUMehtLkrKFgVeSX_Iqbtyws8',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.android.apps.youtube.creator/21.06.103(Linux; U; Android 9; en_GB; VirtualBox Build/PI)',
        origin     = 'studio.youtube.com',
    ),
)
