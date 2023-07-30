import random
import time

from innertube import InnerTube


def delay():
    # A random duration between 2s and 5s
    secs = random.randint(2000, 5000) / 1000

    time.sleep(secs)


channel_browse_id = "UCXuqSBlHAE6Xw-yeJA0Tunw"  # Linus Tech Tips

# Client for YouTube (Web)
client = InnerTube("WEB", "2.20230728.00.00")

# Fetch the browse data for the channel
channel_data = client.browse(channel_browse_id)

# Extract the tab renderer for the "Videos" tab of the channel
videos_tab_renderer = channel_data["contents"]["twoColumnBrowseResultsRenderer"][
    "tabs"
][1]["tabRenderer"]

# Make sure this tab is the "Videos" tab
assert videos_tab_renderer["title"] == "Videos"

# Extract the browse params for the "Videos" tab of the channel
videos_params = videos_tab_renderer["endpoint"]["browseEndpoint"]["params"]

# Wait a bit so that Google doesn't suspect us of being a bot
delay()

# Fetch the browse data for the channel's videos
videos_data = client.browse(channel_browse_id, params=videos_params)

# Extract the rich video items and the continuation item
*rich_items, continuation_item = videos_data["contents"][
    "twoColumnBrowseResultsRenderer"
]["tabs"][1]["tabRenderer"]["content"]["richGridRenderer"]["contents"]

# Loop through each video and log out its details
for rich_item in rich_items:
    video_renderer = rich_item["richItemRenderer"]["content"]["videoRenderer"]

    video_id = video_renderer["videoId"]
    video_title = video_renderer["title"]["runs"][0]["text"]

    print(f"[{video_id}] {video_title}")

# Extract the continuation token
continuation_token = continuation_item["continuationItemRenderer"][
    "continuationEndpoint"
]["continuationCommand"]["token"]

# Fetch more videos by using the continuation token
more_videos_data = client.browse(continuation=continuation_token)


