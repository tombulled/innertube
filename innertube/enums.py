import enum

import humps

class StrEnum(str, enum.Enum): pass

class AutoName(StrEnum):
    _generate_next_value_ = lambda name, *_: name

class AutoNameLower(StrEnum):
    _generate_next_value_ = lambda name, *_: name.lower()

class NoValue(AutoName):
    def __repr__(self) -> str:
        return f'<{self.__class__.__name__}.{self.name}>'

# class Host(StrEnum):
#     YOUTUBEI:        str = 'youtubei.googleapis.com'
#     SUGGEST_QUERIES: str = 'suggestqueries.google.com'

class Request(AutoName):
    _generate_next_value_ = lambda name, *_: humps.pascalize(name.lower())

    CONFIG:                                str = enum.auto()
    SEARCH:                                str = enum.auto()
    PLAYER:                                str = enum.auto()
    HOME:                                  str = enum.auto()
    CHANNEL_PAGE:                          str = enum.auto()
    PLAYLIST:                              str = enum.auto()
    WATCH_NEXT:                            str = enum.auto()
    BROWSE_HOME_PAGE:                      str = enum.auto()
    BROWSE_ARTIST_DETAIL_PAGE:             str = enum.auto()
    BROWSE_ALBUM_DETAIL_PAGE:              str = enum.auto()
    BROWSE_PLAYLIST_DETAIL_PAGE:           str = enum.auto()
    BROWSE_EXPLORE_PAGE:                   str = enum.auto()
    BROWSE_NEW_RELEASES_PAGE:              str = enum.auto()
    BROWSE_CHARTS_PAGE:                    str = enum.auto()
    BROWSE_MOODS_AND_GENRES_PAGE:          str = enum.auto()
    BROWSE_MOODS_AND_GENRES_CATEGORY_PAGE: str = enum.auto()
    MUSIC_GUIDE:                           str = enum.auto()
    MUSIC_QUEUE:                           str = enum.auto()
    MUSIC_WATCH_NEXT:                      str = enum.auto()
    MUSIC_SEARCH_SUGGESTIONS:              str = enum.auto()
    MOBILE_MAIN_APP_GUIDE:                 str = enum.auto()
    WEB_MAIN_APP_GUIDE:                    str = enum.auto()

class RequestContext(AutoNameLower):
    CHANNEL_CREATOR: str = enum.auto()

class BrowseId(StrEnum):
    _generate_next_value_ = lambda name, *_: f'FE{name.lower()}'

    MUSIC_EXPLORE                   = enum.auto()
    MUSIC_NEW_RELEASES              = enum.auto()
    MUSIC_CHARTS                    = enum.auto()
    MUSIC_HOME                      = enum.auto()
    MUSIC_MOODS_AND_GENRES          = enum.auto()
    MUSIC_MOODS_AND_GENRES_CATEGORY = enum.auto()

class Company(NoValue):
    GOOGLE: str = enum.auto()

class Product(NoValue):
    MOZILLA: str = enum.auto()

class Host(NoValue):
    YOUTUBEI:        str = enum.auto()
    SUGGEST_QUERIES: str = enum.auto()

class Api(NoValue):
    YOUTUBEI_V1:     str = enum.auto()
    SUGGEST_QUERIES: str= enum.auto()

class Device(NoValue):
    WEB:     str = enum.auto()
    ANDROID: str = enum.auto()
    IOS:     str = enum.auto()
    TV:      str = enum.auto()

class Service(NoValue):
    YOUTUBE:        str = enum.auto()
    YOUTUBE_MUSIC:  str = enum.auto()
    YOUTUBE_KIDS:   str = enum.auto()
    YOUTUBE_STUDIO: str = enum.auto()

class Client(NoValue):
    WEB:             str = enum.auto()
    WEB_REMIX:       str = enum.auto()
    WEB_KIDS:        str = enum.auto()
    WEB_CREATOR:     str = enum.auto()
    ANDROID:         str = enum.auto()
    ANDROID_MUSIC:   str = enum.auto()
    ANDROID_KIDS:    str = enum.auto()
    ANDROID_CREATOR: str = enum.auto()
    IOS:             str = enum.auto()
    IOS_MUSIC:       str = enum.auto()
    IOS_KIDS:        str = enum.auto()
    IOS_CREATOR:     str = enum.auto()
    TVHTML5:         str = enum.auto()

class Alt(AutoNameLower):
    JSON: str = enum.auto()

class Scheme(AutoNameLower):
    HTTP:  str = enum.auto()
    HTTPS: str = enum.auto()

class Method(AutoName):
    GET:     str = enum.auto()
    POST:    str = enum.auto()
    DELETE:  str = enum.auto()
    HEAD:    str = enum.auto()
    OPTIONS: str = enum.auto()
    PATCH:   str = enum.auto()
    PUT:     str = enum.auto()

class Header(StrEnum):
    _generate_next_value_ = lambda name, *_: name.replace('_', '-').title()

    USER_AGENT:      str = enum.auto()
    REFERER:         str = enum.auto()
    CONTENT_TYPE:    str = enum.auto()
    ACCEPT_LANGUAGE: str = enum.auto()

class GoogleHeader(StrEnum):
    _generate_next_value_ = lambda name, *_: 'X-Goog-' + name.replace('_', '-').title()

    VISITOR_ID: str = enum.auto()

class YouTubeHeader(StrEnum):
    _generate_next_value_ = lambda name, *_: 'X-YouTube-' + name.replace('_', '-').title()

    CLIENT_NAME:    str = enum.auto()
    CLIENT_VERSION: str = enum.auto()

class MediaSubtype(AutoNameLower):
    JSON: str = enum.auto()
    HTML: str = enum.auto()

class CharBool(StrEnum):
    _generate_next_value_ = lambda name, *_: name[0].lower()

    TRUE:  str = enum.auto()
    FALSE: str = enum.auto()

class DataSource(StrEnum):
    YOUTUBE: str = 'yt'
