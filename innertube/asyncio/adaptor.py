from typing import Optional

from httpx import AsyncClient, Request, Response

from innertube import api
from innertube.config import config
from innertube.errors import RequestError, ResponseError
from innertube.models import ClientContext


class AsyncInnerTubeAdaptor:
    context: ClientContext
    session: AsyncClient

    def __init__(
        self, context: ClientContext, session: Optional[AsyncClient] = None
    ) -> None:
        self.context = context
        self.session = session or AsyncClient(base_url=config.base_url)

    def __repr__(self) -> str:
        return f"{type(self).__name__}(context={self.context!r})"

    def _build_request(
        self, endpoint: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> Request:
        return self.session.build_request(
            "POST",
            endpoint,
            params=self.context.params().update(params or {}),
            json=api.contextualise(self.context, body or {}),
            headers=self.context.headers(),
        )

    async def _request(
        self, endpoint: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> Response:
        r = self._build_request(endpoint, params=params, body=body)
        return await self.session.send(r)

    async def dispatch(
        self, endpoint: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> dict:
        response: Response = await self._request(endpoint, params=params, body=body)

        content_type: Optional[str] = response.headers.get("Content-Type")

        if content_type is not None:
            if not content_type.lower().startswith("application/json"):
                raise ResponseError(f"Expected JSON response, got {content_type!r}")

        response_data: dict = response.json()

        visitor_data: Optional[str] = response_data.get("responseContext", {}).get(
            "visitorData"
        )

        if visitor_data is not None:
            self.session.headers["X-Goog-Visitor-Id"] = visitor_data

        error: Optional[dict] = response_data.get("error")

        if error is not None:
            raise RequestError(api.error(error))

        return response_data

    # needed for python versions 3.8>= <=3.10 issue from httpx
    # https://github.com/encode/httpx/issues/914
    async def close(self) -> None:
        await self.session.aclose()
