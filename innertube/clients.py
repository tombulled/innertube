from . import adaptor
from . import services

class BaseClient(object):
    adaptor: adaptor.Adaptor

    def __init__(self, service: services.Service):
        self.adaptor = adaptor.Adaptor(service)

    def __repr__(self):
        return f'<Client({self.adaptor.service.client.to_string()})>'

class Web(BaseClient):
    def __init__(self):
        super().__init__(services.WEB)

class WebRemix(BaseClient):
    def __init__(self):
        super().__init__(services.WEB_REMIX)

class WebKids(BaseClient):
    def __init__(self):
        super().__init__(services.WEB_KIDS)

class WebCreator(BaseClient):
    def __init__(self):
        super().__init__(services.WEB_CREATOR)

class Android(BaseClient):
    def __init__(self):
        super().__init__(services.ANDROID)

class AndroidMusic(BaseClient):
    def __init__(self):
        super().__init__(services.ANDROID_MUSIC)

class AndroidKids(BaseClient):
    def __init__(self):
        super().__init__(services.ANDROID_KIDS)

class AndroidCreator(BaseClient):
    def __init__(self):
        super().__init__(services.ANDROID_CREATOR)

class Ios(BaseClient):
    def __init__(self):
        super().__init__(services.IOS)

class IosMusic(BaseClient):
    def __init__(self):
        super().__init__(services.IOS_MUSIC)

class IosKids(BaseClient):
    def __init__(self):
        super().__init__(services.IOS_KIDS)

class IosCreator(BaseClient):
    def __init__(self):
        super().__init__(services.IOS_CREATOR)
