from dataclasses import dataclass, field
from typing import List, Optional

import mediate

from . import api, utils
from .adaptor import InnerTubeAdaptor
from .enums import Endpoint
from .models import ClientContext, Locale
from .protocols import Adaptor


@dataclass
class Client:
    adaptor: Adaptor

    middleware: mediate.Middleware = field(
        default_factory=mediate.Middleware, repr=False, init=False
    )

    def __call__(
        self, endpoint: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> dict:
        @self.middleware.bind
        def process(data: dict, /) -> dict:
            return data

        response: dict = process(
            self.adaptor.dispatch(endpoint, params=params, body=body)
        )

        response.pop("responseContext")

        return response


@dataclass(init=False)
class InnerTube(Client):
    def __init__(
        self,
        client_name: str,
        client_version: Optional[str] = None,
        *,
        api_key: Optional[str] = None,
        user_agent: Optional[str] = None,
        referer: Optional[str] = None,
        locale: Optional[Locale] = None,
        auto: bool = True,
    ):
        kwargs: dict = utils.filter(
            dict(
                api_key=api_key,
                user_agent=user_agent,
                referer=referer,
                locale=locale,
            )
        )

        if auto and client_version is None:
            client_context: Optional[ClientContext] = api.get_context(client_name)

            if client_context is not None:
                client_version = client_context.client_version

        if client_name is None:
            raise ValueError("Precondition failed: Missing client name")
        if client_version is None:
            raise ValueError("Precondition failed: Missing client version")

        context: ClientContext = ClientContext(
            client_name=client_name,
            client_version=client_version,
            **kwargs,
        )

        super().__init__(adaptor=InnerTubeAdaptor(context))

    def config(self) -> dict:
        return self(Endpoint.CONFIG)

    def guide(self) -> dict:
        return self(Endpoint.GUIDE)

    def player(self, video_id: str) -> dict:
        return self(
            Endpoint.PLAYER,
            body=dict(
                videoId=video_id,
            ),
        )

    def browse(
        self,
        browse_id: Optional[str] = None,
        *,
        params: Optional[str] = None,
        continuation: Optional[str] = None,
    ) -> dict:
        return self(
            Endpoint.BROWSE,
            params=utils.filter(
                dict(
                    continuation=continuation,
                    ctoken=continuation,
                )
            ),
            body=utils.filter(
                dict(
                    browseId=browse_id,
                    params=params,
                )
            ),
        )

    def search(
        self,
        query: Optional[str] = None,
        *,
        params: Optional[str] = None,
        continuation: Optional[str] = None,
    ) -> dict:
        return self(
            Endpoint.SEARCH,
            params=utils.filter(
                dict(
                    continuation=continuation,
                    ctoken=continuation,
                )
            ),
            body=utils.filter(
                dict(
                    query=query or "",
                    params=params,
                )
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
    ) -> dict:
        return self(
            Endpoint.NEXT,
            body=utils.filter(
                dict(
                    params=params,
                    playlistId=playlist_id,
                    videoId=video_id,
                    index=index,
                    continuation=continuation,
                )
            ),
        )

    def music_get_search_suggestions(
        self,
        input: Optional[None] = None,
    ) -> dict:
        return self(
            Endpoint.MUSIC_GET_SEARCH_SUGGESTIONS,
            body=dict(
                input=input or "",
            ),
        )

    def music_get_queue(
        self,
        *,
        video_ids: Optional[List[str]] = None,
        playlist_id: Optional[str] = None,
    ) -> dict:
        return self(
            Endpoint.MUSIC_GET_QUEUE,
            body=utils.filter(
                dict(
                    playlistId=playlist_id,
                    videoIds=video_ids or (None,),
                )
            ),
        )
