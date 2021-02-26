import innertube
from pprint import pprint as pp

from innertube import utils, types

from typing import Union

from innertube import maps, info

c = utils.get_client \
(
    service = innertube.services.YouTubeMusic,
    device  = innertube.devices.Android,
)
