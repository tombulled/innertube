from typing import Any, Optional, Union

import addict
import httpx
import mediatype

from . import enums, errors, models


class BaseSession(httpx.Client):
    def __repr__(self) -> str:
        return f"{type(self).__name__}(base_url={str(self.base_url)!r})"


class JSONSession(BaseSession):
    def send(self, request: httpx.Request, **kwargs: Any) -> httpx.Response:
        response: httpx.Response = super().send(request, **kwargs)

        content_type: mediatype.MediaType = mediatype.parse(
            response.headers.get(str(enums.Header.CONTENT_TYPE))
        )

        if content_type.subtype != mediatype.MediaTypeSubtype.JSON:
            if not response.is_success:
                raise errors.RequestError(models.Error.from_response(response))

            raise errors.ResponseError(
                "Expected response of type {expected_type!r}, got {actual_type!r}".format(
                    expected_type=mediatype.MediaType(
                        type=mediatype.MediaTypeType.APPLICATION,
                        subtype=mediatype.MediaTypeSubtype.JSON,
                        suffix=None,
                        parameters=None,
                    ).string(),
                    actual_type=content_type.string(
                        suffix=False,
                        parameters=False,
                    ),
                ),
            )

        return response


class InnerTubeSession(JSONSession):
    context: dict

    def __init__(
        self,
        *args: Any,
        base_url: str = "https://youtubei.googleapis.com/youtubei/v1/",
        context: Optional[dict] = None,
        **kwargs: Any,
    ):
        super().__init__(*args, base_url=base_url, **kwargs)

        self.context = context or {}

    def __repr__(self) -> str:
        return f"{type(self).__name__}(base_url={str(self.base_url)!r}, context={self.context})"

    def build_request(self, method: str, *args: Any, json: Any = None, **kwargs: Any):
        if method == enums.Method.POST and self.context:
            json = addict.Dict(json or {})

            json.context.client.update(self.context)

        return super().build_request(method, *args, json=json, **kwargs)

    def send(self, request: httpx.Request, **kwargs: Any) -> httpx.Response:
        response: httpx.Response = super().send(request, **kwargs)

        response_data: addict.Dict = addict.Dict(response.json())

        error: addict.Dict
        if error := response_data.error:
            raise errors.RequestError(
                models.Error(code=error.code, message=error.message)
            )

        visitor_data: Union[addict.Dict, str]
        if visitor_data := response_data.responseContext.visitorData:
            self.headers[str(enums.GoogleHeader.VISITOR_ID)] = visitor_data

        return response
