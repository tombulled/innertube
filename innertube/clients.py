import abc
from typing import Any, Callable, List, Optional

import addict
import attr
import httpx
import roster

from . import errors, models, sessions, utils

attrs = attr.s(
    auto_detect=True,
    auto_attribs=True,
)


@attrs
class BaseClient(abc.ABC):
    session: sessions.BaseSession = attr.ib()

    @abc.abstractmethod
    def __call__(self) -> addict.Dict:
        ...

    def __attrs_post_init__(self) -> None:
        pass


@attrs
class BaseInnerTubeClient(BaseClient):
    session: sessions.InnerTubeSession = attr.ib(
        default=attr.Factory(sessions.InnerTubeSession),
        init=False,
    )

    parsers: roster.Register[
        Callable[[addict.Dict], addict.Dict], models.Parser
    ] = attr.ib(
        default=attr.Factory(roster.Register),
        repr=False,
        init=False,
    )

    def __attrs_post_init__(self) -> None:
        parser: Callable = self.parsers.value(models.Parser)

        @parser()
        def identity(data: addict.Dict, /) -> addict.Dict:
            return data

    def __call__(self, *args: Any, **kwargs: Any) -> addict.Dict:
        response: httpx.Response = self.session.post(*args, **kwargs)

        response_data: addict.Dict = addict.Dict(response.json())

        fingerprint: models.ResponseFingerprint = (
            models.ResponseFingerprint.from_response(response)
        )

        parser: models.Parser = models.Parser.from_response_fingerprints(fingerprint)

        if response_data.responseContext:
            del response_data.responseContext

        parse: Callable[[addict.Dict], addict.Dict]
        schema: models.Parser
        for parse, schema in reversed(self.parsers.items()):
            if not schema.any() or schema.intersect(parser).any():
                return parse(response_data)

        raise errors.NoParserFound(
            f"No parser found for response with fingerprint: {fingerprint!r}"
        )


@attrs
class InnerTubeClient(BaseInnerTubeClient):
    def config(self) -> addict.Dict:
        return self("config")

    def guide(self) -> addict.Dict:
        return self("guide")

    def player(self, *, video_id: str) -> addict.Dict:
        return self(
            "player",
            json=dict(
                videoId=video_id,
            ),
        )

    def browse(
        self,
        browse_id: Optional[str] = None,
        *,
        params: Optional[str] = None,
        continuation: Optional[str] = None,
    ) -> addict.Dict:
        return self(
            "browse",
            params=utils.filter(
                continuation=continuation,
                ctoken=continuation,
            ),
            json=utils.filter(
                browseId=browse_id,
                params=params,
            ),
        )

    def search(
        self,
        query: Optional[str] = None,
        *,
        params: Optional[str] = None,
        continuation: Optional[str] = None,
    ) -> addict.Dict:
        return self(
            "search",
            params=utils.filter(
                continuation=continuation,
                ctoken=continuation,
            ),
            json=utils.filter(
                query=query or "",
                params=params,
            ),
        )

    def next(
        self,
        video_id: Optional[str] = None,
        playlist_id: Optional[str] = None,
        *,
        params: Optional[str] = None,
        index: Optional[int] = None,
        continuation: Optional[str] = None,
    ) -> addict.Dict:
        return self(
            "next",
            json=utils.filter(
                params=params,
                playlistId=playlist_id,
                videoId=video_id,
                index=index,
                continuation=continuation,
            ),
        )

    def music_get_search_suggestions(
        self,
        input: Optional[None] = None,
    ) -> addict.Dict:
        return self(
            "music/get_search_suggestions",
            json=dict(
                input=input or "",
            ),
        )

    def music_get_queue(
        self,
        *,
        video_ids: Optional[List[str]] = None,
        playlist_id: Optional[str] = None,
    ) -> addict.Dict:
        return self(
            "music/get_queue",
            json=utils.filter(
                playlistId=playlist_id,
                videoIds=video_ids or (None,),
            ),
        )
