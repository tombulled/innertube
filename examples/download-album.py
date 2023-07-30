from dataclasses import dataclass
from io import BufferedWriter
from pathlib import Path
import random
import time
from typing import Any, Mapping, MutableMapping, MutableSequence, Optional, Sequence

import httpx
import rich
from httpx import Response

from innertube import InnerTube

"""
TODO: Redesign the system - can be simpler

* Locate an album using YouTube Music, e.g. Silhouettes by Aquilo - https://music.youtube.com/playlist?list=OLAK5uy_khNLsz9s6ueH8YHdzORuy4PORu6tWvMrY
* Look up the album as a playlist using YouTube, e.g. https://www.youtube.com/playlist?list=OLAK5uy_khNLsz9s6ueH8YHdzORuy4PORu6tWvMrY
* YouTube provides the full set of songs for that album
* Get a full-res image from YouTube as well

"""


def delay() -> None:
    timeout: float = random.randint(2000, 5000) / 1000

    time.sleep(timeout)


# ARTIST_ID: str = "UCnX0L9QiftAcWdzeBx31xCw"  # Twenty One Pilots
# ALBUM_BROWSE_ID: str = "MPREb_X7QffEAYTTO"  # Blurryface
# ALBUM_BROWSE_ID: str = "MPREb_ScQaLIaWEv5"  # Vessel (with Bonus Tracks)

# ARTIST_ID: str = "UCG_7ydxEUqxJlIL9_Uy-Z4Q"  # Seafret
# ALBUM_BROWSE_ID: str = "MPREb_MCxFDUkd9VE"  # Tell Me It's Real (Expanded Edition)

# ARTIST_ID: str = "UCMO-CgAtd1jI2m2CrXcP2sQ"  # Amber Run
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_lqinhYxeDfCZtbt8N1GdI6aqlj44ThfMU" # Spark EP
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_nB_qEA_pG8EZia0z58eDE25v1i0fpSNH0" # Pilot EP
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_kEH-J7dPuErmAozzG-CTVDOklQIG_xP6g" # 5AM (Expanded Edition)
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_mMR_VYCeV0xhW_Nfo3U2qukj9Y_I0T-wE" # For A Moment, I Was Lost
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_kQrMjMljbR28Ge-EwC8AmTmoN4e1qx24w" # Acoustic EP
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_n0oZXFeNxRvK0ZV6P-_qm2EiEOOoBe_wI" # The Assembly
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_k-nVhxfuIQFO2ZE9EvqPKKM4__S3aOb_Y" # Philophobia
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_kHykDXcCDzpye0foS6E1crEZJRW8uo58A" # The Search (Act I)
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_mL2zfBIO9DFJlHguE0XFv0sZdmar3Wv58" # The Start (Act II)
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_lPqeK5z74imJPGxul-pU_U_6-s0qOctug" # How To Be Human
# ALBUM_BROWSE_ID: str = "MPREb_r8YGYkwyp1n"  # 5AM (Expanded Edition)
# ALBUM_BROWSE_ID: str = "MPREb_JHECxKJ1QJ0"  # For A Moment, I Was Lost
# ALBUM_BROWSE_ID: str = "MPREb_9JEV6UNu4aT"  # Philophobia
# ALBUM_BROWSE_ID: str = "MPREb_Xt0H2hDGuqA"  # The Search (Act I)

# ARTIST_ID: str = "UCItuxDxh9AO1P2Miiso_0tg"  # Aquilo
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_mdZx9ip6w7LcOwL4LsLJY1ewjoERMeJGs" # In The Low Light (Live)
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_m9x1ATvvF-BHUVbEW0XyTdrzbtC_WxsrM" # Live From RAK Studios
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_nCyEX0Zzgd22KA07Z8LUZ3STLktKMbWYQ" # Aquilo
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_lnohUgmn9QftycLEqIqQZli57FSf2AvWY" # Human
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_nx04vFkplXV9X85by-8mP46JLmTNqweW0" # Calling Me
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_msaMtkKquZeUqQ6sMOr0kk6TQydo9cZYY" # Midnight (Live EP)
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_khNLsz9s6ueH8YHdzORuy4PORu6tWvMrY" # Silhouettes
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_nAHK5zWEf-pf-3KXSj93NA8ZGyjTBfJUg" # ii
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_lW66eJCF7wQ4hhtHkTYjYy1Wh-ctYE8lY" # ii (Reworks)
# ALBUM_PLAYLIST_ID: str = "OLAK5uy_kRjXobVjFEz323V44CIfuKCKRngWX-Ogg" # A Safe Place To Be
ALBUM_PLAYLIST_ID: str = "OLAK5uy_ndMEnXwNd0HkeljYKBuzKHoHpJB3NX8mU" # Sober EP
# ALBUM_BROWSE_ID: str = "MPREb_XEoOYtkwx3X"  # ii
# ALBUM_BROWSE_ID: str = "MPREb_eHA1ouWw7fU"  # Silhouettes
# ALBUM_BROWSE_ID: str = "MPREb_5s8ufeIeDGW"  # Sober EP

# ARTIST_ID: str = "UC8Yu1_yfN5qPh601Y4btsYw"  # Arctic Monkeys
# ALBUM_BROWSE_ID: str = "MPREb_m7saomf2NFN"  # AM
# ALBUM_BROWSE_ID: str = "MPREb_1X7jgKSpSz7"  # Whatever People Say I Am, That's What I Am Not

# ARTIST_ID: str = "UCLEJF57HPNem3bdqXSiIo3Q"  # Band of Horses
# ALBUM_BROWSE_ID: str = "MPREb_ij6eHbvH9FF"  # Why Are You OK
# ALBUM_BROWSE_ID: str = "MPREb_ISeBtatD8ky"  # Cease to Begin
# ALBUM_BROWSE_ID: str = "MPREb_ctJ5HEJw8pg"  # Everything All The Time


@dataclass
class Song:
    name: str
    video_id: str


@dataclass
class Artist:
    name: str
    browse_id: str


@dataclass
class Album:
    browse_id: str
    name: str
    description: str
    thumbnail: str
    year: int
    artist: Artist
    tracks: Sequence[Song]


@dataclass
class ArtistPage:
    artist: Artist
    songs_playlist_id: str


@dataclass
class ShortAlbum:
    browse_id: str
    name: str


@dataclass
class PlaylistSong:
    id: str
    name: str
    thumbnail: str
    artist: Artist
    album: Optional[ShortAlbum] = None


@dataclass
class PlaylistPage:
    id: str
    name: str
    thumbnail: str
    songs: Sequence[PlaylistSong]
    channel_name: Optional[str] = None


def get_artist_page(artist_browse_id: str, /) -> ArtistPage:
    client: InnerTube = InnerTube("IOS_MUSIC")

    data: dict = client.browse(artist_browse_id)

    artist_name: str = data["header"]["musicVisualHeaderRenderer"]["title"]["runs"][0][
        "text"
    ]

    raw_shelves: Sequence[Mapping[str, Mapping[str, Any]]] = data["contents"][
        "singleColumnBrowseResultsRenderer"
    ]["tabs"][0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"]

    shelves: MutableMapping[str, Any] = {}

    raw_shelf: Mapping[str, Any]
    for raw_shelf in raw_shelves:
        shelf_key: str = next(iter(raw_shelf.keys()))

        shelves.setdefault(shelf_key, []).append(raw_shelf[shelf_key])

    songs_playlist_id: str = shelves["musicShelfRenderer"][0]["moreContentButton"][
        "buttonRenderer"
    ]["navigationEndpoint"]["browseEndpoint"]["browseId"]

    return ArtistPage(
        artist=Artist(
            name=artist_name,
            browse_id=artist_browse_id,
        ),
        songs_playlist_id=songs_playlist_id,
    )


def get_playlist_page(
    playlist_id: str, /, *, params: Optional[str] = None
) -> PlaylistPage:
    client: InnerTube = InnerTube("WEB_REMIX")

    data: dict = client.browse(playlist_id, params=params)

    playlist_name: str = data["header"]["musicDetailHeaderRenderer"]["title"]["runs"][
        0
    ]["text"]
    playlist_thumbnail: str = data["header"]["musicDetailHeaderRenderer"]["thumbnail"][
        "croppedSquareThumbnailRenderer"
    ]["thumbnail"]["thumbnails"][-1]["url"]

    playlist_tracks: MutableSequence[PlaylistSong] = []

    shelf_items = data["contents"]["singleColumnBrowseResultsRenderer"]["tabs"][0][
        "tabRenderer"
    ]["content"]["sectionListRenderer"]["contents"][0]["musicPlaylistShelfRenderer"][
        "contents"
    ]

    for shelf_item in shelf_items:
        song_video_id: str = shelf_item["musicResponsiveListItemRenderer"][
            "playlistItemData"
        ]["videoId"]
        song_thumbnail: str = shelf_item["musicResponsiveListItemRenderer"][
            "thumbnail"
        ]["musicThumbnailRenderer"]["thumbnail"]["thumbnails"][-1]["url"]
        song_name: str = shelf_item["musicResponsiveListItemRenderer"]["flexColumns"][
            0
        ]["musicResponsiveListItemFlexColumnRenderer"]["text"]["runs"][0]["text"]
        song_artist_name: str = shelf_item["musicResponsiveListItemRenderer"][
            "flexColumns"
        ][1]["musicResponsiveListItemFlexColumnRenderer"]["text"]["runs"][0]["text"]
        song_artist_browse_id: str = shelf_item["musicResponsiveListItemRenderer"][
            "flexColumns"
        ][1]["musicResponsiveListItemFlexColumnRenderer"]["text"]["runs"][0][
            "navigationEndpoint"
        ][
            "browseEndpoint"
        ][
            "browseId"
        ]

        song_album: Optional[ShortAlbum] = None

        if shelf_item["musicResponsiveListItemRenderer"]["flexColumns"][2][
            "musicResponsiveListItemFlexColumnRenderer"
        ]["text"]:
            song_album_name: str = shelf_item["musicResponsiveListItemRenderer"][
                "flexColumns"
            ][2]["musicResponsiveListItemFlexColumnRenderer"]["text"]["runs"][0]["text"]
            song_album_browse_id: str = shelf_item["musicResponsiveListItemRenderer"][
                "flexColumns"
            ][2]["musicResponsiveListItemFlexColumnRenderer"]["text"]["runs"][0][
                "navigationEndpoint"
            ][
                "browseEndpoint"
            ][
                "browseId"
            ]

            song_album = ShortAlbum(
                name=song_album_name,
                browse_id=song_album_browse_id,
            )

        playlist_tracks.append(
            PlaylistSong(
                id=song_video_id,
                name=song_name,
                thumbnail=song_thumbnail,
                artist=Artist(
                    name=song_artist_name,
                    browse_id=song_artist_browse_id,
                ),
                album=song_album,
            )
        )

    return PlaylistPage(
        id=playlist_id,
        name=playlist_name,
        thumbnail=playlist_thumbnail,
        songs=playlist_tracks,
    )


def get_yt_playlist_page(playlist_id: str, /) -> PlaylistPage:
    client: InnerTube = InnerTube("WEB")

    data: dict = client.browse("VL" + playlist_id)

    playlist_video_list_renderer: dict = data["contents"]["twoColumnBrowseResultsRenderer"]["tabs"][0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0]["itemSectionRenderer"]["contents"][0]["playlistVideoListRenderer"]
    playlist_header_renderer: dict = data["header"]["playlistHeaderRenderer"]
    playlist_sidebar_primary_info_renderer: dict = data["sidebar"]["playlistSidebarRenderer"]["items"][0]["playlistSidebarPrimaryInfoRenderer"]
    microformat_data_renderer: dict = data["microformat"]["microformatDataRenderer"]

    phr_playlist_id: str = playlist_header_renderer["playlistId"]
    phr_thumbnail_url: str = playlist_header_renderer["playlistHeaderBanner"]["heroPlaylistThumbnailRenderer"]["thumbnail"]["thumbnails"][-1]["url"]
    phr_title: str = playlist_header_renderer["title"]["simpleText"]
    phr_subtitle: str = playlist_header_renderer["subtitle"]["simpleText"]

    pspir_thumbnail_url: str = playlist_sidebar_primary_info_renderer["thumbnailRenderer"]["playlistCustomThumbnailRenderer"]["thumbnail"]["thumbnails"][-1]["url"]

    mf_thumbnail_url: str = microformat_data_renderer["thumbnail"]["thumbnails"][-1]["url"]

    pvlr_playlist_id: str = playlist_video_list_renderer["playlistId"]

    pvlr_songs = []

    for playlist_video_renderer in playlist_video_list_renderer["contents"]:
        playlist_video_renderer = playlist_video_renderer["playlistVideoRenderer"]

        pvr_video_id: str = playlist_video_renderer["videoId"]
        pvr_thumbnail_url: str = playlist_video_renderer["thumbnail"]["thumbnails"][-1]["url"]
        pvr_title: str = playlist_video_renderer["title"]["runs"][0]["text"]
        pvr_index: str = playlist_video_renderer["index"]["simpleText"]
        pvr_channel_name: str = playlist_video_renderer["shortBylineText"]["runs"][0]["text"]
        pvr_channel_id: str = playlist_video_renderer["shortBylineText"]["runs"][0]["navigationEndpoint"]["browseEndpoint"]["browseId"]
        pvr_length: str = playlist_video_renderer["lengthSeconds"]

        pvlr_songs.append(
            PlaylistSong(
                id=pvr_video_id,
                name=pvr_title,
                thumbnail=pvr_thumbnail_url,
                artist=Artist(
                    name=pvr_channel_name,
                    browse_id=pvr_channel_id,
                ),
            )
        )

    return PlaylistPage(
        id=phr_playlist_id,
        name=phr_title.split(" - ", 1)[1],
        channel_name=phr_subtitle.split(" • ", 1)[0],
        thumbnail=phr_thumbnail_url,
        songs=pvlr_songs,
    )


def get_album(browse_id: str, /) -> Album:
    client: InnerTube = InnerTube("IOS_MUSIC")

    album: dict = client.browse(browse_id)

    album_name: str = album["header"]["musicDetailHeaderRenderer"]["title"]["runs"][0][
        "text"
    ]
    album_description: str = album["header"]["musicDetailHeaderRenderer"]["byline"][
        "musicDetailHeaderButtonsBylineRenderer"
    ]["description"]["runs"][0]["text"]
    album_thumbnail: str = album["header"]["musicDetailHeaderRenderer"]["thumbnail"][
        "croppedSquareThumbnailRenderer"
    ]["thumbnail"]["thumbnails"][-1]["url"]
    album_year: int = int(
        album["header"]["musicDetailHeaderRenderer"]["subtitle"]["runs"][-1]["text"]
    )
    album_artist_name: str = album["header"]["musicDetailHeaderRenderer"][
        "secondTitle"
    ]["runs"][-1]["text"]
    album_artist_browse_id: str = album["header"]["musicDetailHeaderRenderer"][
        "secondTitle"
    ]["runs"][-1]["navigationEndpoint"]["browseEndpoint"]["browseId"]

    tracks: MutableSequence[Song] = []

    for music_shelf_item in album["contents"]["singleColumnBrowseResultsRenderer"][
        "tabs"
    ][0]["tabRenderer"]["content"]["sectionListRenderer"]["contents"][0][
        "musicShelfRenderer"
    ][
        "contents"
    ]:
        song_name: str = music_shelf_item["musicTwoColumnItemRenderer"]["title"][
            "runs"
        ][0]["text"]
        song_video_id: str = music_shelf_item["musicTwoColumnItemRenderer"][
            "navigationEndpoint"
        ]["watchEndpoint"]["videoId"]

        tracks.append(
            Song(
                name=song_name,
                video_id=song_video_id,
            )
        )

    return Album(
        name=album_name,
        description=album_description,
        thumbnail=album_thumbnail,
        year=album_year,
        browse_id=browse_id,
        artist=Artist(
            name=album_artist_name,
            browse_id=album_artist_browse_id,
        ),
        tracks=tracks,
    )


def get_video_stream_url(video_id: str, /) -> Optional[str]:
    client: InnerTube = InnerTube("IOS_MUSIC")

    data: dict = client.player(video_id)

    optimal_stream_url: Optional[str] = None
    optimal_stream_bitrate: Optional[int] = None

    stream: dict
    for stream in data["streamingData"]["adaptiveFormats"]:
        if not stream["mimeType"].startswith("audio/mp4"):
            continue

        if optimal_stream_url is None or stream["bitrate"] > optimal_stream_bitrate:
            optimal_stream_url = stream["url"]
            optimal_stream_bitrate = stream["bitrate"]

    return optimal_stream_url


def download(url: str, path: Path) -> None:
    response: Response
    file: BufferedWriter
    with httpx.stream("GET", url) as response, path.open("ab") as file:
        data: bytes
        for data in response.iter_bytes(chunk_size=8196):
            file.write(data)


# artist_page: ArtistPage = get_artist_page(ARTIST_ID)

# delay()

# top_songs = get_playlist_page(artist_page.songs_playlist_id)

# albums: MutableMapping[str, MutableSequence[PlaylistSong]] = {}

# song: PlaylistSong
# for song in top_songs.songs:
#     if song.album is None:
#         continue

#     albums.setdefault(song.album.browse_id, []).append(song)

# album_songs: Mapping[str, str] = {
#     album_song.name: album_song.id for album_song in albums[ALBUM_BROWSE_ID]
# }

# delay()
# album: Album = get_album(ALBUM_BROWSE_ID)

# fixed_album_tracks: Sequence[Song] = [
#     Song(name=album_track.name, video_id=album_songs[album_track.name])
#     for album_track in album.tracks
# ]

playlist: PlaylistPage = get_yt_playlist_page(ALBUM_PLAYLIST_ID)

rich.print(f"Downloading: {playlist.name!r} by {playlist.channel_name!r}")

music_dir: Path = Path.home() / "Music"

album_dir: Path = music_dir / Path(f"{playlist.channel_name} - {playlist.name}")

if not album_dir.exists():
    album_dir.mkdir()

album_thumbnail_path: Path = album_dir.joinpath("thumbnail.jpg")

if not album_thumbnail_path.exists():
    download(playlist.thumbnail, album_thumbnail_path)

total_tracks: int = len(playlist.songs)

index: int
track: PlaylistSong
for index, track in enumerate(playlist.songs):
    track_path: Path = album_dir.joinpath(f"{str(index+1).zfill(2)} - {track.name}.m4a")

    if track_path.exists():
        continue

    delay()
    track_url: Optional[str] = get_video_stream_url(track.id)

    if track_url is None:
        continue

    rich.print(f"\t ({str(index+1).zfill(2)}/{str(total_tracks).zfill(2)}) {track.name!r}")

    delay()
    # download(track_url, track_path)

    import os

    os.system(f'wget -q "{track_url}" -O "{track_path}"')
