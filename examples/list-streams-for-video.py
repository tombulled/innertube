from innertube import InnerTube
from pprint import pprint

# Rick Astley - Never Gonna Give You Up (Official Music Video)
video_id = "dQw4w9WgXcQ"

# Client for YouTube on iOS
client = InnerTube("IOS")

# Fetch the player data for the video
data = client.player(video_id)

# List of streams of the video
streams = data["streamingData"]["adaptiveFormats"]

# Print the list of streams
pprint(streams)
