'''
Library containing every InnerTube Client

Each Client has been coupled with it's associated ClientInfo, so is able to construct
itself correctly when instantiated

>>> from innertube.clients import clients
>>>
>>> dir(clients)
...
>>>
>>> clients.Web
<class 'innertube.clients.clients.Web'>
>>>
'''

from .. import infos
from . import services
from . import devices
from .decorators import info

@info(infos.clients.Web)
class Web(devices.WebClient, services.YouTubeClient):
    '''
    InnerTube Client: Web

    Device:  Web
    Service: YouTube
    '''

    ...

@info(infos.clients.WebMusic)
class WebMusic(devices.WebClient, services.YouTubeMusicClient):
    '''
    InnerTube Client: WebMusic

    Device:  Web
    Service: YouTube Music
    '''

    ...

@info(infos.clients.WebKids)
class WebKids(devices.WebClient, services.YouTubeKidsClient):
    '''
    InnerTube Client: WebKids

    Device:  Web
    Service: YouTube Kids
    '''

    ...

@info(infos.clients.WebStudio)
class WebStudio(devices.WebClient, services.YouTubeStudioClient):
    '''
    InnerTube Client: WebStudio

    Device:  Web
    Service: YouTube Studio
    '''

    ...

@info(infos.clients.Android)
class Android(devices.AndroidClient, services.YouTubeClient):
    '''
    InnerTube Client: Android

    Device:  Android
    Service: YouTube
    '''

    ...

@info(infos.clients.AndroidMusic)
class AndroidMusic(devices.AndroidClient, services.YouTubeMusicClient):
    '''
    InnerTube Client: AndroidMusic

    Device:  Android
    Service: YouTube Music
    '''

    ...

@info(infos.clients.AndroidKids)
class AndroidKids(devices.AndroidClient, services.YouTubeKidsClient):
    '''
    InnerTube Client: AndroidKids

    Device:  Android
    Service: YouTube Kids
    '''

    ...

@info(infos.clients.AndroidStudio)
class AndroidStudio(devices.AndroidClient, services.YouTubeStudioClient):
    '''
    InnerTube Client: AndroidStudio

    Device:  Android
    Service: YouTube Studio
    '''

    ...

@info(infos.clients.Ios)
class Ios(devices.IosClient, services.YouTubeClient):
    '''
    InnerTube Client: Ios

    Device:  Ios
    Service: YouTube
    '''

    ...

@info(infos.clients.IosMusic)
class IosMusic(devices.IosClient, services.YouTubeMusicClient):
    '''
    InnerTube Client: IosMusic

    Device:  Ios
    Service: YouTube Music
    '''

    ...

@info(infos.clients.IosKids)
class IosKids(devices.IosClient, services.YouTubeKidsClient):
    '''
    InnerTube Client: IosKids

    Device:  Ios
    Service: YouTube Kids
    '''

    ...

@info(infos.clients.IosStudio)
class IosStudio(devices.IosClient, services.YouTubeStudioClient):
    '''
    InnerTube Client: IosStudio

    Device:  Ios
    Service: YouTube Studio
    '''

    ...

@info(infos.clients.Tv)
class Tv(devices.TvClient, services.YouTubeClient):
    '''
    InnerTube Client: Tv

    Device:  Tv
    Service: YouTube
    '''

    ...
