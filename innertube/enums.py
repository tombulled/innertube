import enum

class StrEnum(str, enum.Enum): pass

class AutoName(StrEnum):
    _generate_next_value_ = lambda name, *_: name

class AutoNameLower(StrEnum):
    _generate_next_value_ = lambda name, *_: name.lower()

class Company(AutoName):
    GOOGLE = enum.auto()

class Product(AutoName):
    MOZILLA = enum.auto()

class Host(AutoName):
    YOUTUBEI        = enum.auto()
    SUGGEST_QUERIES = enum.auto()

class Api(AutoName):
    YOUTUBEI_V1     = enum.auto()
    SUGGEST_QUERIES = enum.auto()

class Device(AutoName):
    WEB     = enum.auto()
    ANDROID = enum.auto()
    IOS     = enum.auto()
    TV      = enum.auto()

class Service(AutoName):
    YOUTUBE        = enum.auto()
    YOUTUBE_MUSIC  = enum.auto()
    YOUTUBE_KIDS   = enum.auto()
    YOUTUBE_STUDIO = enum.auto()

class Client(AutoName):
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

class App(AutoName):
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

class Method(AutoName):
    GET  = enum.auto()
    POST = enum.auto()
    # ...

class Header(StrEnum):
    _generate_next_value_ = lambda name, *_: name.replace('_', '-').title()

    USER_AGENT     = enum.auto()
    REFERER        = enum.auto()
    CONTENT_TYPE   = enum.auto()
    VISITOR_ID     = 'X-Goog-Visitor-Id'
    CLIENT_NAME    = 'X-YouTube-Client-Name'
    CLIENT_VERSION = 'X-YouTube-Client-Version'

class MediaSubtype(AutoNameLower):
    JSON = enum.auto()
    HTML = enum.auto()

class CharBool(StrEnum):
    _generate_next_value_ = lambda name, *_: name[0].lower()

    TRUE  = enum.auto()
    FALSE = enum.auto()

class Encoding(StrEnum):
    _generate_next_value_ = lambda name, *_: name.replace('_', '-').lower()

    UTF_8 = enum.auto()

class DataSource(StrEnum):
    YOUTUBE = 'yt'
