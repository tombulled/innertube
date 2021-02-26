from . import base

class YouTubeClient(base.Client):
    def guide(self):
        return self('guide')

class YouTubeMusicClient(base.Client):
    def guide(self):
        return self('guide')

class YouTubeKidsClient(base.Client):
    # Not implemented: guide

    pass

class YouTubeStudioClient(base.Client):
    pass
