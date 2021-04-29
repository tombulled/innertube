import furl
import slugify

import enumb

class BaseDomain(enumb.AutoStrEnum):
    def reverse(self):
        return '.'.join(reversed(self.split('.')))

    def url(self):
        return str \
        (
            furl.furl \
            (
                scheme = Scheme.HTTPS,
                host   = self,
                path   = '/',
            )
        )

class Domain(BaseDomain):
    _generate_next_value_ = lambda name, *_: name.replace('_', '').lower() + '.com'

    GOOGLE:       str
    GOOGLE_APIS:  str
    YOUTUBE:      str
    YOUTUBE_KIDS: str

class Host(BaseDomain):
    YOUTUBEI:        str = f'youtubei.{Domain.GOOGLE_APIS}'
    SUGGEST_QUERIES: str = f'suggestqueries.{Domain.GOOGLE}'
    YOUTUBE:         str = f'www.{Domain.YOUTUBE}'
    YOUTUBE_MUSIC:   str = f'music.{Domain.YOUTUBE}'
    YOUTUBE_STUDIO:  str = f'studio.{Domain.YOUTUBE}'
    YOUTUBE_KIDS:    str = f'www.{Domain.YOUTUBE_KIDS}'

class Request(enumb.AutoNamePascal):
    CONFIG:                                str
    SEARCH:                                str
    PLAYER:                                str
    HOME:                                  str
    CHANNEL_PAGE:                          str
    PLAYLIST:                              str
    WATCH_NEXT:                            str
    BROWSE_HOME_PAGE:                      str
    BROWSE_ARTIST_DETAIL_PAGE:             str
    BROWSE_ALBUM_DETAIL_PAGE:              str
    BROWSE_PLAYLIST_DETAIL_PAGE:           str
    BROWSE_EXPLORE_PAGE:                   str
    BROWSE_NEW_RELEASES_PAGE:              str
    BROWSE_CHARTS_PAGE:                    str
    BROWSE_MOODS_AND_GENRES_PAGE:          str
    BROWSE_MOODS_AND_GENRES_CATEGORY_PAGE: str
    MUSIC_GUIDE:                           str
    MUSIC_QUEUE:                           str
    MUSIC_WATCH_NEXT:                      str
    MUSIC_SEARCH_SUGGESTIONS:              str
    MOBILE_MAIN_APP_GUIDE:                 str
    WEB_MAIN_APP_GUIDE:                    str

class RequestContext(enumb.AutoNameLower):
    CHANNEL_CREATOR: str

class BrowseId(enumb.AutoStrEnum):
    _generate_next_value_ = lambda name, *_: f'FE{name.lower()}'

    MUSIC_EXPLORE:                   str
    MUSIC_NEW_RELEASES:              str
    MUSIC_CHARTS:                    str
    MUSIC_HOME:                      str
    MUSIC_MOODS_AND_GENRES:          str
    MUSIC_MOODS_AND_GENRES_CATEGORY: str

class ErrorStatus(enumb.AutoName):
    PERMISSION_DENIED:   str
    INVALID_ARGUMENT:    str
    FAILED_PRECONDITION: str
    NOT_FOUND:           str

class Company(enumb.AutoNameTitle):
    GOOGLE:  str

class ProductName(enumb.AutoNameTitle):
    MOZILLA:  str

class Product(enumb.StrEnum):
    def __new__(cls, name, version):
        obj = str.__new__(cls, name)

        obj._value_ = name
        obj.version = version

        return obj

    MOZILLA: str = ('Mozilla', '5.0')

class BaseEntity(enumb.AutoName):
    def slug(self):
        return slugify.slugify(self)

class GoogleClient(enumb.AutoNameSlug):
    YOUTUBE:               str
    YOUTUBE_PEGASUS_WEB:   str
    YOUTUBE_MUSIC_ANDROID: str
    YOUTUBE_MUSIC_IOS:     str
    YOUTUBE_LR:            str

class Device(enumb.AutoNameLower):
    WEB:     str
    ANDROID: str
    IOS:     str
    LR:      str

class DeviceFamily(enumb.AutoName):
    WEB:    str
    MOBILE: str

class Service(enumb.AutoNameSlug):
    YOUTUBE:        str
    YOUTUBE_MUSIC:  str
    YOUTUBE_KIDS:   str
    YOUTUBE_STUDIO: str

class Client(enumb.AutoName):
    WEB:             str
    WEB_REMIX:       str
    WEB_KIDS:        str
    WEB_CREATOR:     str
    ANDROID:         str
    ANDROID_MUSIC:   str
    ANDROID_KIDS:    str
    ANDROID_CREATOR: str
    IOS:             str
    IOS_MUSIC:       str
    IOS_KIDS:        str
    IOS_CREATOR:     str
    TVHTML5:         str

class ClientId(enumb.IntEnum):
    WEB:         int = 1
    WEB_REMIX:   int = 62
    WEB_KIDS:    int = 67
    WEB_CREATOR: int = 76

class Alt(enumb.AutoNameLower):
    JSON: str

class Scheme(enumb.AutoNameLower):
    HTTP:  str
    HTTPS: str

class Method(enumb.AutoName):
    PUT:     str
    GET:     str
    POST:    str
    HEAD:    str
    PATCH:   str
    DELETE:  str
    OPTIONS: str

class Header(enumb.AutoNameSlugTitle):
    USER_AGENT:      str
    REFERER:         str
    CONTENT_TYPE:    str
    ACCEPT_LANGUAGE: str
    AUTHORIZATION:   str

class GoogleHeader(enumb.AutoNameSlugTitle):
    _generate_next_value_ = lambda name, *_: f'X-Goog-{enumb.AutoNameSlugTitle._generate_next_value_(name)}'

    VISITOR_ID:         str
    DEVICE_AUTH:        str
    API_FORMAT_VERSION: str

class YouTubeHeader(enumb.AutoNameSlugTitle):
    _generate_next_value_ = lambda name, *_: f'X-YouTube-{enumb.AutoNameSlugTitle._generate_next_value_(name)}'

    CLIENT_NAME:    str
    CLIENT_VERSION: str

class Bool(enumb.AutoStrEnum):
    _generate_next_value_ = lambda name, *_: name[0].lower()

    TRUE:  str
    FALSE: str

class DataSource(enumb.AutoStrEnum):
    YOUTUBE: str = 'yt'
