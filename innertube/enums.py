import enum

class StrEnum(str, enum.Enum): pass

class AutoName(StrEnum):
    def _generate_next_value_(name: str, *_) -> str:
        return name

class AutoNameLower(StrEnum):
    def _generate_next_value_(name: str, *_) -> str:
        return name.lower()

class DeviceType(AutoName):
    WEB     = enum.auto()
    ANDROID = enum.auto()
    IOS     = enum.auto()
    TV      = enum.auto()

class ServiceType(AutoName):
    YOUTUBE        = enum.auto()
    YOUTUBE_MUSIC  = enum.auto()
    YOUTUBE_KIDS   = enum.auto()
    YOUTUBE_STUDIO = enum.auto()

class ClientType(AutoName):
    WEB            = enum.auto()
    WEB_MUSIC      = enum.auto()
    WEB_KIDS       = enum.auto()
    WEB_STUDIO     = enum.auto()
    ANDROID        = enum.auto()
    ANDROID_MUSIC  = enum.auto()
    ANDROID_KIDS   = enum.auto()
    ANDROID_STUDIO = enum.auto()
    IOS            = enum.auto()
    IOS_MUSIC      = enum.auto()
    IOS_KIDS       = enum.auto()
    IOS_STUDIO     = enum.auto()
    TV             = enum.auto()

class AppType(AutoName):
    YOUTUBE_WEB            = enum.auto()
    YOUTUBE_MUSIC_WEB      = enum.auto()
    YOUTUBE_KIDS_WEB       = enum.auto()
    YOUTUBE_STUDIO_WEB     = enum.auto()
    YOUTUBE_ANDROID        = enum.auto()
    YOUTUBE_MUSIC_ANDROID  = enum.auto()
    YOUTUBE_KIDS_ANDROID   = enum.auto()
    YOUTUBE_STUDIO_ANDROID = enum.auto()
    YOUTUBE_IOS            = enum.auto()
    YOUTUBE_MUSIC_IOS      = enum.auto()
    YOUTUBE_KIDS_IOS       = enum.auto()
    YOUTUBE_STUDIO_IOS     = enum.auto()
    YOUTUBE_TV             = enum.auto()

class Alt(AutoNameLower):
    JSON = enum.auto()

class Scheme(AutoNameLower):
    HTTP  = enum.auto()
    HTTPS = enum.auto()

class Header(StrEnum):
    USER_AGENT     = 'User-Agent'
    REFERER        = 'Referer'
    CONTENT_TYPE   = 'Content-Type'
    VISITOR_ID     = 'X-Goog-Visitor-Id'
    CLIENT_NAME    = 'X-YouTube-Client-Name'
    CLIENT_VERSION = 'X-YouTube-Client-Version'

class Mime(StrEnum):
    JSON = 'application/json'
    HTML = 'text/html'

class CharBool(StrEnum):
    TRUE  = 't'
    FALSE = 'f'

class Encoding(StrEnum):
    UTF_8 = 'utf-8'

class DataSource(StrEnum):
    YOUTUBE = 'yt'
