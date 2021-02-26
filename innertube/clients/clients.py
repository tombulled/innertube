from . import devices
from . import services
from .. import infos

class Web(devices.WebClient, services.YouTubeClient):
    def __init__(self):
        super().__init__(infos.Web)

class WebMusic(devices.WebClient, services.YouTubeMusicClient):
    def __init__(self):
        super().__init__(infos.WebMusic)

class WebKids(devices.WebClient, services.YouTubeKidsClient):
    def __init__(self):
        super().__init__(infos.WebKids)

class WebStudio(devices.WebClient, services.YouTubeStudioClient):
    def __init__(self):
        super().__init__(infos.WebStudio)

class Android(devices.AndroidClient, services.YouTubeClient):
    def __init__(self):
        super().__init__(infos.Android)

class AndroidMusic(devices.AndroidClient, services.YouTubeMusicClient):
    def __init__(self):
        super().__init__(infos.AndroidMusic)

class AndroidKids(devices.AndroidClient, services.YouTubeKidsClient):
    def __init__(self):
        super().__init__(infos.AndroidKids)

class AndroidStudio(devices.AndroidClient, services.YouTubeStudioClient):
    def __init__(self):
        super().__init__(infos.AndroidStudio)

class Ios(devices.IosClient, services.YouTubeClient):
    def __init__(self):
        super().__init__(infos.Ios)

class IosMusic(devices.IosClient, services.YouTubeMusicClient):
    def __init__(self):
        super().__init__(infos.IosMusic)

class IosKids(devices.IosClient, services.YouTubeKidsClient):
    def __init__(self):
        super().__init__(infos.IosKids)

class IosStudio(devices.IosClient, services.YouTubeStudioClient):
    def __init__(self):
        super().__init__(infos.IosStudio)
