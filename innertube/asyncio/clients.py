import dataclasses
from typing import List, Optional, Coroutine

import httpx
import mediate
from httpx._types import ProxiesTypes

from innertube import api, utils
from .adaptor import AsyncInnerTubeAdaptor
from innertube.config import config
from innertube.enums import Endpoint
from innertube.models import ClientContext, Locale
from innertube.protocols import AsyncAdaptor


@dataclasses.dataclass
class AsyncClient:
    adaptor: AsyncAdaptor

    middleware: mediate.Middleware = dataclasses.field(
        default_factory=mediate.Middleware, repr=False, init=False
    )

    def __call__(
        self,
        endpoint: str,
        params: Optional[dict] = None,
        body: Optional[dict] = None,
    ) -> Coroutine:
        @self.middleware.bind
        async def process(data: Coroutine, /) -> Coroutine:
            _data = await data
            _data.pop("responseContext")
            return _data

        response: Coroutine = process(
            self.adaptor.dispatch(endpoint, params=params, body=body)
        )

        return response


@dataclasses.dataclass(init=False)
class InnerTube(AsyncClient):
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
            adaptor=AsyncInnerTubeAdaptor(
                context=context,
                session=httpx.AsyncClient(base_url=config.base_url, proxies=proxies),
            ),
        )

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.close()

    async def config(self) -> dict:
        return await self(Endpoint.CONFIG)

    async def guide(self) -> dict:
        return await self(Endpoint.GUIDE)

    async def player(self, video_id: str) -> dict:
        return await self(
            Endpoint.PLAYER,
            body=dict(
                videoId=video_id,
            ),
        )

    async def browse(
        self,
        browse_id: Optional[str] = None,
        *,
        params: Optional[str] = None,
        continuation: Optional[str] = None,
    ) -> dict:
        return await self(
            Endpoint.BROWSE,
            body=utils.filter(
                dict(
                    browseId=browse_id,
                    params=params,
                    continuation=continuation,
                )
            ),
        )

    async def search(
        self,
        query: Optional[str] = None,
        *,
        params: Optional[str] = None,
        continuation: Optional[str] = None,
    ) -> dict:
        return await self(
            Endpoint.SEARCH,
            body=utils.filter(
                dict(
                    query=query or "",
                    params=params,
                    continuation=continuation,
                )
            ),
        )

    async def next(
        self,
        video_id: Optional[str] = None,
        playlist_id: Optional[str] = None,
        *,
        params: Optional[str] = None,
        index: Optional[int] = None,
        continuation: Optional[str] = None,
    ) -> dict:
        return await self(
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

    async def get_transcript(
        self,
        params: str,
    ) -> dict:
        return await self(
            Endpoint.GET_TRANSCRIPT,
            body=utils.filter(
                dict(
                    params=params,
                )
            ),
        )

    async def music_get_search_suggestions(
        self,
        input: Optional[None] = None,
    ) -> dict:
        return await self(
            Endpoint.MUSIC_GET_SEARCH_SUGGESTIONS,
            body=dict(
                input=input or "",
            ),
        )

    async def music_get_queue(
        self,
        *,
        video_ids: Optional[List[str]] = None,
        playlist_id: Optional[str] = None,
    ) -> dict:
        return await self(
            Endpoint.MUSIC_GET_QUEUE,
            body=utils.filter(
                dict(
                    playlistId=playlist_id,
                    videoIds=video_ids or (None,),
                )
            ),
        )

    async def close(self) -> None:
        await self.adaptor.close()
