import innertube
from pprint import pprint as pp

web       = innertube.Web()
web_remix = innertube.WebRemix()

android       = innertube.Android()
android_music = innertube.AndroidMusic()

ios       = innertube.Ios()
ios_music = innertube.IosMusic()

import pydantic
import enum

class Device(enum.Enum):
    Web     = 'web'
    Android = 'android'
    Ios     = 'ios'

class Service(enum.Enum):
    YouTube       = 'youtube'
    YouTubeMusic  = 'youtube.music'
    YouTubeKids   = 'youtube.kids'
    YouTubeStudio = 'youtube.creator'

# from innertube.services import *
# from innertube import adaptor

# a = adaptor.Adaptor(ANDROID_CREATOR)

# pp(a.dispatch('browse', payload = {'browseId': 'FEvideo_manager'}))
# pp(a.dispatch('guide'))
