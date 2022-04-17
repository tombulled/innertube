import enumb


class Request(enumb.Pascal):
    CONFIG: str
    SEARCH: str
    PLAYER: str
    HOME: str
    CHANNEL_PAGE: str
    PLAYLIST: str
    WATCH_NEXT: str
    BROWSE_HOME_PAGE: str
    BROWSE_ARTIST_DETAIL_PAGE: str
    BROWSE_ALBUM_DETAIL_PAGE: str
    BROWSE_PLAYLIST_DETAIL_PAGE: str
    BROWSE_EXPLORE_PAGE: str
    BROWSE_NEW_RELEASES_PAGE: str
    BROWSE_CHARTS_PAGE: str
    BROWSE_MOODS_AND_GENRES_PAGE: str
    BROWSE_MOODS_AND_GENRES_CATEGORY_PAGE: str
    MUSIC_GUIDE: str
    MUSIC_QUEUE: str
    MUSIC_WATCH_NEXT: str
    MUSIC_SEARCH_SUGGESTIONS: str
    MOBILE_MAIN_APP_GUIDE: str
    WEB_MAIN_APP_GUIDE: str


class RequestContext(enumb.Snake):
    CHANNEL_CREATOR: str


class BrowseId(enumb.StrEnum):
    _generate_next_value_ = lambda name, *_: f"FE{name.lower()}"

    # Youtube Music
    MUSIC_EXPLORE: str
    MUSIC_NEW_RELEASES: str
    MUSIC_CHARTS: str
    MUSIC_HOME: str
    MUSIC_MOODS_AND_GENRES: str
    MUSIC_MOODS_AND_GENRES_CATEGORY: str
    # YouTube
    WHAT_TO_WATCH: str
    SHORTS: str
    LIBRARY: str
    # YouTube Kids
    KIDS_HOME: str


class ErrorStatus(enumb.Macro):
    PERMISSION_DENIED: str
    INVALID_ARGUMENT: str
    FAILED_PRECONDITION: str
    NOT_FOUND: str


class ClientScreen(enumb.Macro):
    EMBED: str


class Header(enumb.Train):
    USER_AGENT: str
    REFERER: str
    CONTENT_TYPE: str
    ACCEPT_LANGUAGE: str
    AUTHORIZATION: str


class GoogleHeader(enumb.Train):
    _generate_next_value_ = (
        lambda name, *_: f"X-Goog-{enumb.Train._generate_next_value_(name, -1, -1, [])}"
    )

    VISITOR_ID: str
    DEVICE_AUTH: str
    API_FORMAT_VERSION: str


class YouTubeHeader(enumb.Train):
    _generate_next_value_ = (
        lambda name, *_: f"X-YouTube-{enumb.Train._generate_next_value_(name, -1, -1, [])}"
    )

    CLIENT_NAME: str
    CLIENT_VERSION: str
