import innertube
from pprint import pprint as pp

c = innertube.client \
(
    service = innertube.services.YouTubeMusic,
    device  = innertube.devices.Android,
)
