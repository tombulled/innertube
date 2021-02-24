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
        version = '2.20200516.07.00',
    ),
    api = Api \
    (
        key     = 'AIzaSyAO_FJ2SlqU8Q4STEHLGCilw_Y9_11qcW8',
        domain  = 'youtubei.googleapis.com',
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
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
        origin     = 'music.youtube.com',
    ),
)

ANDROID = Service \
(
    client = Client \
    (
        name    = 'ANDROID',
        version = '15.19.34',
    ),
    api = Api \
    (
        key     = 'AIzaSyA8eiZmM1FaDVjRy-df2KTyQ_vz_yYM39w',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.android.youtube/15.19.34(Linux; U; Android 5.1.1; en_UK; SM-G930K Build/NRD90M)',
        origin     = 'www.youtube.com',
    ),
)

ANDROID_MUSIC = Service \
(
    client = Client \
    (
        name    = 'ANDROID_MUSIC',
        version = '3.65.58',
    ),
    api = Api \
    (
        key     = 'AIzaSyCbNu0kKlAVm5mL6m4NUEgCUl0NR3nPqLs',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.android.apps.youtube.music/3.65.58(Linux; U; Android 5.1.1; en_UK; SM-G930K Build/NRD90M)',
        origin     = 'music.youtube.com',
    ),
)

IOS = Service \
(
    client = Client \
    (
        name    = 'IOS',
        version = '15.19.4',
    ),
    api = Api \
    (
        key     = 'AIzaSyB-63vPrdThhKuerbB2N_l7Kwwcxj6yUAc',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.ios.youtube/15.19.4 (iPhone10,5; U; CPU iOS 13_4_1 like Mac OS X; en_GB)',
        origin     = 'www.youtube.com',
    ),
)

IOS_MUSIC = Service \
(
    client = Client \
    (
        name    = 'IOS_MUSIC',
        version = '3.65.3',
    ),
    api = Api \
    (
        key     = 'AIzaSyDK3iBpDP9nHVTk2qL73FLJICfOC3c51Og',
        domain  = 'youtubei.googleapis.com',
        version = 1,
    ),
    adaptor = Adaptor \
    (
        user_agent = 'com.google.ios.youtubemusic/3.65.3 (iPhone10,5; U; CPU iOS 13_4_1 like Mac OS X; en_GB)',
        origin     = 'music.youtube.com',
    ),
)
