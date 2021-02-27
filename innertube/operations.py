import requests
import json
import re
import urllib.parse
from . import utils
from .infos import services
from typing import List

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
        raise Exception(data) # Return a custom exception?

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

def complete_search(query: str) -> List[str]:
    response = requests.get \
    (
        url = utils.url \
        (
            domain   = 'suggestqueries.google.com',
            endpoint = 'complete/search',
        ),
        params = \
        {
            'q':      query,
            'client': 'youtube-lr',
            'hl':     'en',
            'gl':     'gb',
            'ds':     'yt',
            'oe':     'utf-8',
            'xhr':    't',
        },
    )

    return [suggestion for suggestion, _ in response.json()[1]]
