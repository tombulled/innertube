import enum

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
