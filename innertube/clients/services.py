from . import base

class YouTubeClient(base.Client):
    def guide(self):
        return self('guide')

class YouTubeMusicClient(base.Client):
    def guide(self):
        return self('guide')

    def music_get_search_suggestions(self):
        ... # TODO: client('music/get_search_suggestions', payload = {'input': 'foo'})

    def music_get_queue(self):
        ... # TODO: client('music/get_queue', payload = utils.filter({'playlistId': None, 'videoIds': 'XXYlFuWEuKI'}))

class YouTubeKidsClient(base.Client):
    pass

class YouTubeStudioClient(base.Client):
    pass
