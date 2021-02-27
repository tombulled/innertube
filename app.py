import innertube
from pprint import pprint as pp

'''
NOTES:
* Fix clash between Client and ClientInfo properly :/
'''

from innertube import maps, utils

web = maps.CLIENTS['Web']()
ps4 = maps.CLIENTS['Tv']()

def dispatch(client):
    return client('search', payload = {'query': 'foo'})

'''
for client in maps.CLIENTS.values():
    client = client()

    print(client)

    try:
        resp = dispatch(client)

        print(str(resp)[:100])
        # pp(resp)
    except Exception as error:
        print(error)

    print()
'''

import requests
import json

def complete_search(query, music=True):
    url = utils.url \
    (
        domain   = 'suggestqueries.google.com',
        endpoint = 'complete/search',
    )

    # Move this to constants?
    clients = \
    {
        'youtube': \
        {
            'web': 'youtube',
            'ios': 'youtube-ios-pb',
            'android': 'youtube-android-pb',
        },
        'youtube_music': \
        {
            'ios': 'youtube-music-ios-v2',
            'android': 'youtube-music-android-v2',
        },
    }

    if music:
        client = clients['youtube_music']['android']
    else:
        client = clients['youtube']['web']

    resp = requests.get \
    (
        url = url,
        params = \
        {
            'q': query,
            'client': client,
            'hl': 'en-GB',
            'gl': 'GB',
            'ds': 'yt',
            'oe': 'UTF-8',
            'hjson': 't',
            'xssi': 't',
            'gs_pcr': 't',
        },
    )

    if resp.status_code != 200:
        soup = bs4.BeautifulSoup(resp.text, 'html.parser')

        title = soup.find('title')
        bold = soup.find('b')
        paragraph = soup.find_all('p')[-1]
        insert = paragraph.find('ins')

        error_title = title.text.strip()

        error_status_match = re.search(r'\((.+)\)', error_title)

        if error_status_match:
            error_status = error_status_match.group(1)
        else:
            error_status = error_title.split()[0]

        error_status = error_status.upper().replace(' ', '_')

        error_code = int(bold.text.strip().replace('.', ''))
        error_reason = paragraph.text.strip().replace(insert.text, '')

        error = \
        {
            'errorcode': error_code,
            'reason': error_reason,
            'status': error_status,
        }

        raise Exception(error) # Should be proper error

    data = resp.text.splitlines()[-1]
    data = json.loads(data)

    suggestions = []

    for suggestion, weight in data[1]:
        suggestions.append(suggestion)

    return suggestions

# print(complete_search('foo'))
