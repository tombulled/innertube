'''
Library containing Device-based clients

These clients are for implementing methods that are device-specific
(e.g. only found on Android devices)

>>> from innertube.clients import devices
>>>
>>> dir(devices)
...
>>>
>>> devices.WebClient
<class 'innertube.clients.devices.WebClient'>
>>>
'''

from . import base

class WebClient(base.Client):
    '''
    Class to be inheritied by clients meeting the criteria:
        Device: Web
    '''

    ...

class AndroidClient(base.Client):
    '''
    Class to be inheritied by clients meeting the criteria:
        Device: Android
    '''

    ...

class IosClient(base.Client):
    '''
    Class to be inheritied by clients meeting the criteria:
        Device: Ios
    '''

    ...

class TvClient(base.Client):
    '''
    Class to be inheritied by clients meeting the criteria:
        Device: Tv
    '''

    ...
