import innertube
from pprint import pprint as pp

'''
Endpoints:
    guide
        Yes:
            <Client(device='Android', service='YouTube')>
            <Client(device='Android', service='YouTube Music')>
            <Client(device='IOS', service='YouTube')>
            <Client(device='IOS', service='YouTube Music')>
            <Client(device='Web', service='YouTube')>
            <Client(device='Web', service='YouTube Music')>
        No:
            <Client(device='Android', service='YouTube Kids')>
            <Client(device='IOS', service='YouTube Kids')>
            <Client(device='Web', service='YouTube Kids')>
        Maybe (Authentication error):
            <Client(device='Android', service='YouTube Studio')>
            <Client(device='IOS', service='YouTube Studio')>
            <Client(device='Web', service='YouTube Studio')>
    config
        Yes:
            All
    browse:
        Yes:
            All (not tested with specific browseIds)
    search:
        Yes:
            All except IosStudio and AndoidStudio (500 - backendError, INTERNAL)
    next:
        Yes:
            All except IosStudio and AndoidStudio (400 - CONDITION_NOT_MET, INVALID_ARGUMENT)
    player:
        Yes:
            All
    log_event:
        Yes:
            All

TODO Endpoints:
    feedback
    offline (requires authentication)
    notification_registration/get_settings
    notification_registration/set_registration
    visitor_id (works on all, what's it used for?)

    deviceregistration/v1/devices (root-level endpoint)

    # Account related?
    account/accounts_list
    account/get_setting (can be requested unauthenticated)
    /account/account_menu
    ypc/get_offline_upsell
    ypc/log_payment_server_analytics
    browse/edit_playlist
    like/like
    history/get_history_paused_state

    verify_session (not an 'api' endpoint, sticks on end of domain)

    $search suggestions (non-music ones, uses suggestqueries.google.com)
    $requesting a page? (config, gets api key)
    $video info (made redundant by 'player'?)
'''

from innertube import maps, utils

web = maps.CLIENTS['Web']()
ps4 = maps.CLIENTS['Tv']()

def dispatch(client):
    return client('next', payload = {'videoId': 'XXYlFuWEuKI'})

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
