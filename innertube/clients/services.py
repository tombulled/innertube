from . import base
from . import methods
from .decorators import method

@method(methods.guide)
@method(methods.search)
@method(methods.next)
class YouTubeClient(base.Client): ...

@method(methods.guide)
@method(methods.search)
@method(methods.next)
@method(methods.music_get_search_suggestions)
@method(methods.music_get_queue)
class YouTubeMusicClient(base.Client): ...

@method(methods.search)
@method(methods.next)
class YouTubeKidsClient(base.Client): ...

class YouTubeStudioClient(base.Client): ...
