import enum


class StrEnum(str, enum.Enum):
    pass


class Endpoint(StrEnum):
    CONFIG: str = "config"
    GUIDE: str = "guide"
    PLAYER: str = "player"
    BROWSE: str = "browse"
    SEARCH: str = "search"
    NEXT: str = "next"
    GET_TRANSCRIPT: str = "get_transcript"
    MUSIC_GET_SEARCH_SUGGESTIONS: str = "music/get_search_suggestions"
    MUSIC_GET_QUEUE: str = "music/get_queue"


class Request(StrEnum):
    CONFIG: str = "Config"
    SEARCH: str = "Search"
    PLAYER: str = "Player"
    HOME: str = "Home"
    CHANNEL_PAGE: str = "ChannelPage"
    PLAYLIST: str = "Playlist"
    WATCH_NEXT: str = "WatchNext"
    BROWSE_HOME_PAGE: str = "BrowseHomePage"
    BROWSE_ARTIST_DETAIL_PAGE: str = "BrowseArtistDetailPage"
    BROWSE_ALBUM_DETAIL_PAGE: str = "BrowseAlbumDetailPage"
    BROWSE_PLAYLIST_DETAIL_PAGE: str = "BrowsePlaylistDetailPage"
    BROWSE_EXPLORE_PAGE: str = "BrowseExplorePage"
    BROWSE_NEW_RELEASES_PAGE: str = "BrowseNewReleasesPage"
    BROWSE_CHARTS_PAGE: str = "BrowseChartsPage"
    BROWSE_MOODS_AND_GENRES_PAGE: str = "BrowseMoodsAndGenresPage"
    BROWSE_MOODS_AND_GENRES_CATEGORY_PAGE: str = "BrowseMoodsAndGenresCategoryPage"
    MUSIC_GUIDE: str = "MusicGuide"
    MUSIC_QUEUE: str = "MusicQueue"
    MUSIC_WATCH_NEXT: str = "MusicWatchNext"
    MUSIC_SEARCH_SUGGESTIONS: str = "MusicSearchSuggestions"
    MOBILE_MAIN_APP_GUIDE: str = "MobileMainAppGuide"
    WEB_MAIN_APP_GUIDE: str = "WebMainAppGuide"


class ErrorStatus(StrEnum):
    FAILED_PRECONDITION: str = "FAILED_PRECONDITION"


class RequestContext(StrEnum):
    CHANNEL_CREATOR: str = "channel_creator"


class BrowseId(StrEnum):
    # Youtube Music
    MUSIC_EXPLORE: str = "FEmusic_explore"
    MUSIC_NEW_RELEASES: str = "FEmusic_new_releases"
    MUSIC_CHARTS: str = "FEmusic_charts"
    MUSIC_HOME: str = "FEmusic_home"
    MUSIC_MOODS_AND_GENRES: str = "FEmusic_moods_and_genres"
    MUSIC_MOODS_AND_GENRES_CATEGORY: str = "FEmusic_moods_and_genres_category"
    # YouTube
    WHAT_TO_WATCH: str = "FEwhat_to_watch"
    SHORTS: str = "FEshorts"
    LIBRARY: str = "FElibrary"
    # YouTube Kids
    KIDS_HOME: str = "FEkids_home"
