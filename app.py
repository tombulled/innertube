import innertube
from pprint import pprint as pp

'''
NOTES:
* Fix clash between Client and ClientInfo properly :/

To explore:
    att/get (sends off channel id, found in YouTube Studio - signed in): ids: [{externalChannelId: 'UC...'}]
    att/esr ^ see above
'''

from innertube import clients, utils

web = clients.CLIENTS['Web']()
ps4 = clients.CLIENTS['Tv']()

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

from innertube import operations

# video_info = operations.video_info('iX-QaNzd-0Y') # Stolen Dance
# pp(video_info)

completed_search = operations.complete_search('foo fi')
pp(completed_search)
