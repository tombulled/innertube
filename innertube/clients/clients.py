from . import services
from . import devices
from .. import infos

class Web(devices.WebClient, services.YouTubeClient):
    def __init__(self):
        super().__init__(infos.clients.Web)

class WebMusic(devices.WebClient, services.YouTubeMusicClient):
    def __init__(self):
        super().__init__(infos.clients.WebMusic)

class WebKids(devices.WebClient, services.YouTubeKidsClient):
    def __init__(self):
        super().__init__(infos.clients.WebKids)

class WebStudio(devices.WebClient, services.YouTubeStudioClient):
    def __init__(self):
        super().__init__(infos.clients.WebStudio)

class Android(devices.AndroidClient, services.YouTubeClient):
    def __init__(self):
        super().__init__(infos.clients.Android)

class AndroidMusic(devices.AndroidClient, services.YouTubeMusicClient):
    def __init__(self):
        super().__init__(infos.clients.AndroidMusic)

class AndroidKids(devices.AndroidClient, services.YouTubeKidsClient):
    def __init__(self):
        super().__init__(infos.clients.AndroidKids)

class AndroidStudio(devices.AndroidClient, services.YouTubeStudioClient):
    def __init__(self):
        super().__init__(infos.clients.AndroidStudio)

class Ios(devices.IosClient, services.YouTubeClient):
    def __init__(self):
        super().__init__(infos.clients.Ios)

class IosMusic(devices.IosClient, services.YouTubeMusicClient):
    def __init__(self):
        super().__init__(infos.clients.IosMusic)

class IosKids(devices.IosClient, services.YouTubeKidsClient):
    def __init__(self):
        super().__init__(infos.clients.IosKids)

class IosStudio(devices.IosClient, services.YouTubeStudioClient):
    def __init__(self):
        super().__init__(infos.clients.IosStudio)
