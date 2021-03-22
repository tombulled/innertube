import enum

class DeviceType(str, enum.Enum):
    WEB     = 'WEB'
    ANDROID = 'ANDROID'
    IOS     = 'IOS'
    TV      = 'TV'

class ServiceType(str, enum.Enum):
    YOUTUBE        = 'YOUTUBE'
    YOUTUBE_MUSIC  = 'YOUTUBE_MUSIC'
    YOUTUBE_KIDS   = 'YOUTUBE_KIDS'
    YOUTUBE_STUDIO = 'YOUTUBE_STUDIO'

class ClientType(str, enum.Enum):
    WEB            = 'WEB'
    WEB_MUSIC      = 'WEB_REMIX'
    WEB_KIDS       = 'WEB_KIDS'
    WEB_STUDIO     = 'WEB_CREATOR'
    ANDROID        = 'ANDROID'
    ANDROID_MUSIC  = 'ANDROID_MUSIC'
    ANDROID_KIDS   = 'ANDROID_KIDS'
    ANDROID_STUDIO = 'ANDROID_CREATOR'
    IOS            = 'IOS'
    IOS_MUSIC      = 'IOS_MUSIC'
    IOS_KIDS       = 'IOS_KIDS'
    IOS_STUDIO     = 'IOS_CREATOR'
    TV             = 'TV'

class Alt(str, enum.Enum):
    JSON = 'json'

class ApiEndpoint(str, enum.Enum):
    CONFIG                       = 'config'
    GUIDE                        = 'guide'
    PLAYER                       = 'player'
    BROWSE                       = 'browse'
    SEARCH                       = 'search'
    NEXT                         = 'next'
    MUSIC_GET_SEARCH_SUGGESTIONS = 'music/get_search_suggestions'
    MUSIC_GET_QUEUE              = 'music/get_queue'

class Header(str, enum.Enum):
    USER_AGENT     = 'User-Agent'
    REFERER        = 'Referer'
    CONTENT_TYPE   = 'Content-Type'
    VISITOR_ID     = 'X-Goog-Visitor-Id'
    CLIENT_NAME    = 'X-YouTube-Client-Name'
    CLIENT_VERSION = 'X-YouTube-Client-Version'

class Mime(str, enum.Enum):
    JSON = 'application/json'
    HTML = 'text/html'

class Scheme(str, enum.Enum):
    HTTP  = 'http'
    HTTPS = 'https'
