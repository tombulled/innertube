from dataclasses import dataclass, field
from typing import Optional

from httpx import Client, Request, Response

from . import api
from .config import config
from .errors import RequestError, ResponseError
from .models import ClientContext


@dataclass
class InnerTubeAdaptor:
    context: ClientContext
    session: Client = field(
        default_factory=lambda: Client(base_url=config.base_url), repr=False
    )

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

    def _request(
        self, endpoint: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> Response:
        return self.session.send(
            self._build_request(endpoint, params=params, body=body)
        )

    def dispatch(
        self, endpoint: str, params: Optional[dict] = None, body: Optional[dict] = None
    ) -> dict:
        response: Response = self._request(endpoint, params=params, body=body)

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
