from innertube import InnerTube
from innertube.config import config
from innertube.utils import find_paths
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("video_id", nargs='?', default="lYBUbBu4W08")
config.base_url = "https://www.youtube.com/youtubei/v1/"
args = parser.parse_args()

web_client = InnerTube("WEB")
remix_client = InnerTube("WEB_REMIX")

# Only the web client returns unauthenticated information about which album playlist a video belongs to
data = web_client.next(video_id=args.video_id)
try:
    # This nested extraction probably easily breaks with API updates, so provide a helpful exception
    # handling to allow easy updates of this code.
    playlist_id = data['engagementPanels'][3]['engagementPanelSectionListRenderer']['content']['structuredDescriptionContentRenderer']['items'][2]['horizontalCardListRenderer']['cards'][0]['videoAttributeViewModel']['secondarySubtitle']['commandRuns'][0]['onTap']['innertubeCommand']['watchPlaylistEndpoint']['playlistId']
except KeyError | IndexError:
    playlist_paths = '\n'.join(find_paths(data, key='playlistId'))
    raise RuntimeError("Playlist id not found in response, is it one of these?\n" + playlist_paths)

playlist_url = f'https://music.youtube.com/playlist?list={playlist_id}'
print('Album playlist URL:', playlist_url)

data = remix_client.resolve_url(url=playlist_url)
endpoint = data['endpoint']['browseEndpoint']

data = remix_client.browse(browse_id=endpoint['browseId'], params=endpoint['params'])

try:
    album_info = (
        data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]
            ["tabRenderer"]["content"]
            ["sectionListRenderer"]["contents"][0]
            ["musicResponsiveHeaderRenderer"])
except KeyError | IndexError:
    header_paths = '\n'.join(find_paths(data, key='musicResponsiveHeaderRenderer'))
    raise RuntimeError("musicResponsiveHeaderRenderer not found in response, is it one of these?\n" + header_paths)

title = album_info["title"]["runs"][0]["text"]
artists = [i["text"] for i in album_info["straplineTextOne"]["runs"]]

print('Album title:', title)
print('Album artists:', artists)
