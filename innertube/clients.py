from . import adaptor
from . import info
from . import infos
import functools

class Client(object):
    adaptor: adaptor.Adaptor

    def __init__(self, client_info: info.ClientInfo):
        self.adaptor = adaptor.Adaptor(client_info)

    def __repr__(self):
        return f'<Client(device={self.info.device.name!r}, service={self.info.service.name!r})>'

    @functools.wraps(adaptor.Adaptor.dispatch)
    def __call__(self, *args, **kwargs):
        return self.adaptor.dispatch(*args, **kwargs)

    @property
    def info(self):
        return self.adaptor.client_info

class YouTubeClient(Client):
    def guide(self):
        return self('guide')

class YouTubeMusicClient(Client):
    def guide(self):
        return self('guide')

class YouTubeKidsClient(Client):
    # Not implemented: guide

    pass

class YouTubeStudioClient(Client):
    pass

class WebClient(Client):
    pass

class AndroidClient(Client):
    pass

class IosClient(Client):
    pass

class Web(WebClient, YouTubeClient):
    def __init__(self):
        super().__init__(infos.Web)

class WebMusic(WebClient, YouTubeMusicClient):
    def __init__(self):
        super().__init__(infos.WebMusic)

class WebKids(WebClient, YouTubeKidsClient):
    def __init__(self):
        super().__init__(infos.WebKids)

class WebStudio(WebClient, YouTubeStudioClient):
    def __init__(self):
        super().__init__(infos.WebStudio)

class Android(AndroidClient, YouTubeClient):
    def __init__(self):
        super().__init__(infos.Android)

class AndroidMusic(AndroidClient, YouTubeMusicClient):
    def __init__(self):
        super().__init__(infos.AndroidMusic)

class AndroidKids(AndroidClient, YouTubeKidsClient):
    def __init__(self):
        super().__init__(infos.AndroidKids)

class AndroidStudio(AndroidClient, YouTubeStudioClient):
    def __init__(self):
        super().__init__(infos.AndroidStudio)

class Ios(IosClient, YouTubeClient):
    def __init__(self):
        super().__init__(infos.Ios)

class IosMusic(IosClient, YouTubeMusicClient):
    def __init__(self):
        super().__init__(infos.IosMusic)

class IosKids(IosClient, YouTubeKidsClient):
    def __init__(self):
        super().__init__(infos.IosKids)

class IosStudio(IosClient, YouTubeStudioClient):
    def __init__(self):
        super().__init__(infos.IosStudio)
