'''
Package to facilitate low-level communication with Google's InnerTube API

Usage:
    >>> import innertube
    >>>
    >>> # Create a client
    >>> client = innertube.client \
    (
        device  = innertube.devices.Web,      # Could also be Android etc.
        service = innertube.services.YouTube, # Could also be YouTubeMusic etc.
    )
    >>>
    >>> # Or... just import the specific one you want
    >>> client = innertube.clients.Web()
    >>>
    >>> # View the client
    >>> client
    <Client(device='Web', service='YouTube')>
    >>>
    >>> # Get some data!
    >>> data = client.search(query = 'foo fighters')
    >>>
    >>> # Power user? No problem, dispatch requests yourself
    >>> data = client('browse', payload = {'browseId': 'FEwhat_to_watch'})
    >>>
    >>> # The core endpoints are implemented, so the above is equivalent to:
    >>> data = client.browse(browse_id = 'FEwhat_to_watch') # A bit cleaner ;)
'''

from . import clients
from .infos import devices
from .infos import services
from .clients.utils import get_client as client
