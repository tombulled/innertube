import dataclasses
from typing import List, Optional

import httpx
import mediate
from httpx._types import ProxiesTypes

from . import api, utils
from .adaptor import InnerTubeAdaptor
from .config import config
from .enums import Endpoint
from .models import ClientContext, Locale
from .protocols import Adaptor


@dataclasses.dataclass
class Client:
    adaptor: Adaptor

    middleware: mediate.Middleware = dataclasses.field(
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


@dataclasses.dataclass(init=False)
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
        proxies: Optional[ProxiesTypes] = None,
    ) -> None:
        if client_name is None:
            raise ValueError("Precondition failed: Missing client name")

        kwargs: dict = utils.filter(
            dict(
                client_name=client_name,
                client_version=client_version,
                api_key=api_key,
                user_agent=user_agent,
                referer=referer,
                locale=locale,
            )
        )

        context: ClientContext

        auto_context: Optional[ClientContext]
        if auto and (auto_context := api.get_context(client_name)):
            context = dataclasses.replace(auto_context, **kwargs)
        else:
            if client_version is None:
                raise ValueError("Precondition failed: Missing client version")

            context = ClientContext(**kwargs)

        super().__init__(
            adaptor=InnerTubeAdaptor(
                context=context,
                session=httpx.Client(base_url=config.base_url, proxies=proxies),
            )
        )

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
            body=utils.filter(
                dict(
                    browseId=browse_id,
                    params=params,
                    continuation=continuation,
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
            body=utils.filter(
                dict(
                    query=query or "",
                    params=params,
                    continuation=continuation,
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
                    playlistIndex=index,
                    continuation=continuation,
                )
            ),
        )

    def get_transcript(
        self,
        params: str,
    ) -> dict:
        return self(
            Endpoint.GET_TRANSCRIPT,
            body=utils.filter(
                dict(
                    params=params,
                )
            ),
        )

    def music_get_search_suggestions(
        self,
        input: Optional[str] = None,
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
