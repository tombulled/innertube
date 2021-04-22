import enumb

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

class Company(enumb.NoValue):
    GOOGLE: str

class Product(enumb.NoValue):
    MOZILLA: str

class Api(enumb.NoValue):
    YOUTUBEI:        str
    SUGGEST_QUERIES: str

class Device(enumb.NoValue):
    WEB:     str
    ANDROID: str
    IOS:     str
    TV:      str

class Service(enumb.NoValue):
    YOUTUBE:        str
    YOUTUBE_MUSIC:  str
    YOUTUBE_KIDS:   str
    YOUTUBE_STUDIO: str

class Client(enumb.NoValue):
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

class GoogleHeader(enumb.AutoNameSlugTitle):
    _generate_next_value_ = lambda name, *_: 'X-Goog-' + enumb.AutoNameSlugTitle._generate_next_value_(name)

    VISITOR_ID: str

class YouTubeHeader(enumb.AutoNameSlugTitle):
    _generate_next_value_ = lambda name, *_: 'X-YouTube-' + enumb.AutoNameSlugTitle._generate_next_value_(name)

    CLIENT_NAME:    str
    CLIENT_VERSION: str

class MediaSubtype(enumb.AutoNameLower):
    JSON: str
    HTML: str

class CharBool(enumb.AutoStrEnum):
    _generate_next_value_ = lambda name, *_: name[0].lower()

    TRUE:  str
    FALSE: str

class DataSource(enumb.AutoStrEnum):
    YOUTUBE: str
