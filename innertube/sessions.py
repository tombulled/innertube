import attr
import requests
import addict

import mime

import typing
import urllib.parse

from . import enums
from . import errors
from . import infos
from . import models

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class Session(requests.Session):
    def __attrs_pre_init__(self):
        super().__init__()

    def __attrs_post_init__(self):
        self.headers[str(enums.Header.USER_AGENT)] = str(infos.devices[enums.Device.WEB].user_agent())

@attrs
class BaseUrlSession(Session):
    base_url: typing.Optional[str] = attr.ib \
    (
        default = None,
        init    = False,
    )

    def __attrs_post_init__(self):
        self.headers[str(enums.Header.REFERER)] = self.base_url

    def prepare_request(self, request: requests.Request) -> requests.PreparedRequest:
        if self.base_url is not None:
            request.url = urllib.parse.urljoin(self.base_url, request.url)

        return super().prepare_request(request)

@attrs
class SuggestQueriesSession(BaseUrlSession):
    base_url: str = attr.ib \
    (
        default = str(infos.hosts[enums.Host.SUGGEST_QUERIES]),
        init    = False,
    )

@attrs
class InnerTubeSession(BaseUrlSession):
    base_url: str = attr.ib \
    (
        default = str(infos.hosts[enums.Host.YOUTUBEI]),
        init    = False,
    )

    context: dict = attr.ib \
    (
        default = attr.Factory(dict),
        init    = False,
    )

    def prepare_request(self, request: requests.Request):
        if self.context and request.method == enums.Method.POST:
            request.json = addict.Dict(request.json or {})

            request.json.context.client.update(self.context)

        return super().prepare_request(request)

    def send(self, request: requests.PreparedRequest, **kwargs) -> requests.Response:
        response = super().send(request, **kwargs)

        content_type = mime.parse(response.headers.get(str(enums.Header.CONTENT_TYPE)))

        if not response.ok:
            if content_type.subtype == mime.MediaSubtype.JSON:
                data = addict.Dict(response.json())

                if (error := data.error):
                    raise errors.HttpException(models.Error.parse_obj(error))

            response.raise_for_status()

        if content_type.subtype == mime.MediaSubtype.JSON:
            data = addict.Dict(response.json())

            if (visitor_data := data.responseContext.visitorData):
                self.headers[str(enums.GoogleHeader.VISITOR_ID)] = visitor_data

        return response
