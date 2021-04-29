import attr
import addict
import requests

import mime

import typing
import urllib.parse

from . import enums
from . import models
from . import infos

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class BaseSession(requests.Session):
    def __attrs_pre_init__(self):
        super().__init__()

@attrs
class BaseUrlSession(BaseSession):
    base_url: typing.Optional[str] = attr.ib \
    (
        default = None,
        init    = False,
    )

    def prepare_request(self, request: requests.Request) -> requests.PreparedRequest:
        if self.base_url is not None:
            request.url = urllib.parse.urljoin(self.base_url, request.url)

        return super().prepare_request(request)

@attrs
class JSONSession(BaseUrlSession):
    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)

        content_type = mime.parse(response.headers.get(str(enums.Header.CONTENT_TYPE)))

        if content_type.subtype != mime.MediaSubtype.JSON:
            if not response.ok:
                # TODO: Make and use a better implementation of this
                response.raise_for_status()

            # TODO: Raise better exception
            raise Exception('response is not json')

        return response

class OuterTubeSession(JSONSession):
    def send(self, *args, **kwargs):
        response = super().send(*args, **kwargs)

        if not response.ok:
            # TODO: Raise better exception
            raise Exception(response.json())

        return response

@attrs
class SuggestQueriesSession(OuterTubeSession):
    base_url: str = attr.ib \
    (
        default = str(infos.apis[enums.Api.SUGGEST_QUERIES]),
        init    = False,
    )

@attrs
class InnerTubeSession(JSONSession):
    base_url: str = attr.ib \
    (
        default = str(infos.apis[enums.Api.YOUTUBEI]),
        init    = False,
    )

    context: dict = attr.ib \
    (
        default = attr.Factory(dict),
        init    = False,
    )

    def prepare_request(self, request):
        if request.method == enums.Method.POST and self.context:
            request.json = addict.Dict(request.json or {})

            request.json.context.client.update(self.context)

        return super().prepare_request(request)

    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)

        response_data = addict.Dict(response.json())

        if (error := response_data.error):
            raise requests.HTTPError(models.Error.parse_obj(error))

        if (visitor_data := response_data.responseContext.visitorData):
            self.headers[str(enums.GoogleHeader.VISITOR_ID)] = visitor_data

        return response
