import requests
import json
import re
import urllib.parse
from typing import List, Union
from . import utils
from . import clients
from . import errors
from .infos import services
from .infos.types import ServiceType
from .infos.models import ServiceInfo

def watch \
        (
            *,
            video_id:    Union[None, str] = None,
            playlist_id: Union[None, str] = None,
            index:       Union[None, int] = None,
        ) -> dict:
    client = clients.Web()

    response = client.adaptor.session.get \
    (
        url = utils.url \
        (
            domain   = client.info.service.domain,
            endpoint = 'watch',
        ),
        params = utils.filter \
        (
            {
                'v':     video_id,
                'list':  playlist_id,
                'index': index,
                'pbj':   1,
            },
        ),
        cookies = \
        {
            'ST-ito1wm': urllib.parse.urlencode \
            (
                {
                    'endpoint': json.dumps \
                    (
                        {
                            'watchEndpoint': utils.filter \
                            (
                                {
                                    'videoId':    video_id,
                                    'playlistId': playlist_id,
                                }
                            ),
                        },
                    ),
                },
            ),
        },
    )

    return response.json()

def video_info(video_id: str) -> dict:
    response = requests.get \
    (
        url = utils.url \
        (
            domain   = services.YouTube.domain,
            endpoint = 'get_video_info',
        ),
        params = \
        {
            'video_id': video_id,
            'el': 'detailpage',
            'ps': 'default',
            'hl': 'en',
            'gl': 'US',
        }
    )

    data = dict(urllib.parse.parse_qsl(response.text))

    if 'errorcode' in data:
        raise errors.InnerTubeException \
        (
            {
                'code':    data.get('errorcode'),
                'status':  data.get('status'),
                'message': data.get('reason'),
            }
        )

    def fflags(data):
        fflags = query_string(data)

        js_types = \
        {
            'true':  True,
            'false': False,
            'null':  None,
        }

        new_fflags = {}

        for fflag_key, fflag_val in fflags.items():
            if fflag_val in js_types:
                fflag_val = js_types[fflag_val]
            elif fflag_val.isdigit():
                fflag_val = int(fflag_val)
            elif re.match(r'^\d+\.\d+$', fflag_val.strip()) is not None:
                fflag_val = float(fflag_val)

            new_fflags[fflag_key] = fflag_val

        return new_fflags

    def csv(data):
        return data.strip(',').split(',')

    def query_string(data):
        return dict(urllib.parse.parse_qsl(data))

    def b64(data):
        return base64.b64decode(data.encode()).decode()

    def boolean(data):
        return bool(int(data))

    def csv_of(type):
        def wrapper(data):
            return list(map(type, csv(data)))

        return wrapper

    parsers = \
    {
        'fexp':                   csv_of(int),
        'fflags':                 fflags,
        'account_playback_token': b64,
        'timestamp':              int,
        'enablecsi':              boolean,
        'use_miniplayer_ui':      boolean,
        'autoplay_count':         int,
        'player_response':        json.loads,
        'watch_next_response':    json.loads,
        'watermark':              csv,
        'rvs':                    query_string,
    }

    for key, value in data.items():
        if key in parsers:
            data[key] = parsers[key](value)

    return data

def complete_search(query: str, *, service: Union[ServiceInfo, ServiceType] = ServiceType.YouTube) -> List[str]:
    service_type = service if isinstance(service, ServiceType) else service.type

    clients = \
    {
        ServiceType.YouTube:      'youtube-lr',               # Uses Device: Tv
        ServiceType.YouTubeMusic: 'youtube-music-android-v2', # Uses Device: Android
        ServiceType.YouTubeKids:  'youtube-pegasus-web',      # Uses Device: Web
    }

    if service_type not in clients:
        service_type = ServiceType.YouTube

    response = requests.get \
    (
        url = utils.url \
        (
            domain   = 'suggestqueries.google.com',
            endpoint = 'complete/search',
        ),
        params = \
        {
            'client': clients.get(service_type),
            'q':      query,
            'hl':     'en',
            'gl':     'gb',
            'ds':     'yt',
            'oe':     'utf-8',
            'xhr':    't',
        },
    )

    return [suggestion for suggestion, _ in response.json()[1]]
