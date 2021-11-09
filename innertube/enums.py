import furl

import enumb

class BaseDomain(enumb.StrEnum):
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

class Request(enumb.Pascal):
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

class RequestContext(enumb.Snake):
    CHANNEL_CREATOR: str

class BrowseId(enumb.StrEnum):
    _generate_next_value_ = lambda name, *_: f'FE{name.lower()}'

    MUSIC_EXPLORE:                   str
    MUSIC_NEW_RELEASES:              str
    MUSIC_CHARTS:                    str
    MUSIC_HOME:                      str
    MUSIC_MOODS_AND_GENRES:          str
    MUSIC_MOODS_AND_GENRES_CATEGORY: str

class ErrorStatus(enumb.Macro):
    PERMISSION_DENIED:   str
    INVALID_ARGUMENT:    str
    FAILED_PRECONDITION: str
    NOT_FOUND:           str

class Company(enumb.Pascal):
    GOOGLE:  str

class ProductName(enumb.Pascal):
    MOZILLA:  str

class Product(enumb.StrEnum):
    def __new__(cls, name, version):
        obj = str.__new__(cls, name)

        obj._value_ = name
        obj.version = version

        return obj

    MOZILLA: str = ('Mozilla', '5.0')

# ref: https://support.google.com/gsa/answer/6329266
class FrontEnd(enumb.Kebab):
    YOUTUBE:               str
    YOUTUBE_PEGASUS_WEB:   str
    YOUTUBE_MUSIC_ANDROID: str
    YOUTUBE_MUSIC_IOS:     str
    YOUTUBE_LR:            str

class Device(enumb.Lower):
    WEB:     str
    ANDROID: str
    IOS:     str
    LR:      str

class DeviceFamily(enumb.Upper):
    WEB:    str
    MOBILE: str

class Service(enumb.Kebab):
    YOUTUBE:        str
    YOUTUBE_MUSIC:  str
    YOUTUBE_KIDS:   str
    YOUTUBE_STUDIO: str

class Client(enumb.Macro):
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
    WEB:                     int = 1
    ANDROID:                 int = 3
    ANDROID_CREATOR:         int = 14
    ANDROID_MUSIC:           int = 21
    ANDROID_EMBEDDED_PLAYER: int = 55
    WEB_REMIX:               int = 62
    WEB_KIDS:                int = 67
    WEB_CREATOR:             int = 76
    WEB_EMBEDDED_PLAYER:     int = 56

class Alt(enumb.Lower):
    JSON: str

class Scheme(enumb.Lower):
    HTTP:  str
    HTTPS: str

class Method(enumb.Upper):
    PUT:     str
    GET:     str
    POST:    str
    HEAD:    str
    PATCH:   str
    DELETE:  str
    OPTIONS: str

class Header(enumb.Train):
    USER_AGENT:      str
    REFERER:         str
    CONTENT_TYPE:    str
    ACCEPT_LANGUAGE: str
    AUTHORIZATION:   str

class GoogleHeader(enumb.Train):
    _generate_next_value_ = lambda name, *_: f'X-Goog-{enumb.Train._generate_next_value_(name, -1, -1, [])}'

    VISITOR_ID:         str
    DEVICE_AUTH:        str
    API_FORMAT_VERSION: str

class YouTubeHeader(enumb.Train):
    _generate_next_value_ = lambda name, *_: f'X-YouTube-{enumb.Train._generate_next_value_(name, -1, -1, [])}'

    CLIENT_NAME:    str
    CLIENT_VERSION: str
