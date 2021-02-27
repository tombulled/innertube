'''
Library containing Service-based clients

These clients are for implementing methods that are service-specific
(e.g. only found in YouTube clients)

>>> from innertube.clients import services
>>>
>>> dir(services)
...
>>>
>>> services.YouTubeClient
<class 'innertube.clients.services.YouTubeClient'>
>>>
'''

from . import base
from . import methods
from .decorators import method

@method(methods.guide)
@method(methods.search)
@method(methods.next)
class YouTubeClient(base.Client):
    '''
    Class to be inheritied by clients meeting the criteria:
        Service: YouTube
    '''

    ...

@method(methods.guide)
@method(methods.search)
@method(methods.next)
@method(methods.music_get_search_suggestions)
@method(methods.music_get_queue)
class YouTubeMusicClient(base.Client):
    '''
    Class to be inheritied by clients meeting the criteria:
        Service: YouTubeMusic
    '''

    ...

@method(methods.search)
@method(methods.next)
class YouTubeKidsClient(base.Client):
    '''
    Class to be inheritied by clients meeting the criteria:
        Service: YouTubeKids
    '''

    ...

class YouTubeStudioClient(base.Client):
    '''
    Class to be inheritied by clients meeting the criteria:
        Service: YouTubeStudio
    '''

    ...
