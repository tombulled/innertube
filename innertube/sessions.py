import requests
import typing
import urllib.parse
import attr
import addict

import mime

from . import enums
from . import errors

@attr.s(init = False)
class BaseUrlSession(requests.Session):
    base_url: typing.Optional[str] = attr.ib(default = None)

    def __init__(self, base_url: typing.Optional[str] = None):
        super().__init__()

        self.base_url = base_url

    def prepare_request(self, request: requests.Request) -> requests.PreparedRequest:
        request.url = urllib.parse.urljoin(self.base_url, request.url)

        return super().prepare_request(request)

@attr.s(init = False)
class BaseSession(requests.Session):
    context: typing.Optional[dict] = attr.ib(default = None)

    def __init__(self, context: typing.Optional[dict] = None):
        super().__init__()

        self.context = context

    def prepare_request(self, request: requests.Request):
        if self.context and request.method == enums.Method.POST:
            request.json = addict.Dict(request.json or {})
            
            request.json.context.client.update(self.context)

        return super().prepare_request(request)

    def send(self, request: requests.PreparedRequest, **kwargs) -> requests.Response:
        response = super().send(request, **kwargs)

        if not response.ok:
            raise errors.InnerTubeException.from_response(response) from None

        if (content_type := response.headers.get(enums.Header.CONTENT_TYPE.value)):
            mime_type = mime.parse(content_type.lower())

            if mime_type.subtype == enums.MediaSubtype.JSON:
                data = addict.Dict(response.json())

                if (visitor_data := data.responseContext.visitorData):
                    self.headers[enums.Header.VISITOR_ID.value] = visitor_data

        return response

@attr.s(init = False)
class Session(BaseUrlSession, BaseSession):
    def __init__(self, base_url: typing.Optional[str] = None, context: typing.Optional[dict] = None):
        super().__init__()

        BaseUrlSession.__init__(self, base_url)
        BaseSession.__init__(self, context)
