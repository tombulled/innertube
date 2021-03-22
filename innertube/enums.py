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
