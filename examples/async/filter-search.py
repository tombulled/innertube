import asyncio
from innertube.asyncio import InnerTube

PARAMS_TYPE_VIDEO = "EgIQAQ%3D%3D"
PARAMS_TYPE_CHANNEL = "EgIQAg%3D%3D"
PARAMS_TYPE_PLAYLIST = "EgIQAw%3D%3D"
PARAMS_TYPE_FILM = "EgIQBA%3D%3D"


async def main() -> None:
    async with InnerTube("WEB", "2.20230920.00.00") as client:
        data = await client.search("arctic monkeys", params=PARAMS_TYPE_PLAYLIST)

        items = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
            "sectionListRenderer"
        ]["contents"][0]["itemSectionRenderer"]["contents"]

        for item in items:
            playlist = item["playlistRenderer"]

            playlist_id = playlist["playlistId"]
            playlist_title = playlist["title"]["simpleText"]
            playlist_video_count = playlist["videoCount"]

            print(f"[{playlist_id}] {playlist_title} ({playlist_video_count} videos)")

    await asyncio.sleep(1)

    # Alternative usage
    client = InnerTube("WEB", "2.20230920.00.00")
    data = await client.search("arctic monkeys", params=PARAMS_TYPE_PLAYLIST)

    items = data["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"][
        "sectionListRenderer"
    ]["contents"][0]["itemSectionRenderer"]["contents"]

    for item in items:
        playlist = item["playlistRenderer"]

        playlist_id = playlist["playlistId"]
        playlist_title = playlist["title"]["simpleText"]
        playlist_video_count = playlist["videoCount"]

        print(f"[{playlist_id}] {playlist_title} ({playlist_video_count} videos)")

    # use this method for python versions 3.8>= <=3.10
    # https://github.com/encode/httpx/issues/914
    await client.close()


asyncio.run(main())
