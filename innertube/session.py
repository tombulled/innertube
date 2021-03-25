import attr
import addict
import requests_toolbelt.sessions

import functools

from . import errors
from . import enums
from . import models

from typing import \
(
    Optional,
)

@attr.s(init = False)
class Session(requests_toolbelt.sessions.BaseUrlSession):
    base_url: str = attr.ib()

    __context: Optional[dict]

    def __init__ \
            (
                self,
                *,
                base_url: Optional[str]  = None,
                context:  Optional[dict] = None,
                headers:  Optional[dict] = None,
                params:   Optional[dict] = None,
            ):
        super().__init__(base_url = base_url)

        self.headers.update(headers or {})
        self.params.update(params or {})

        self.__context = context

    @functools.wraps(requests_toolbelt.sessions.BaseUrlSession.request)
    def request(self, *args, **kwargs) -> addict.Dict:
        if (context := self.__context):
            kwargs = addict.Dict(kwargs)

            if not kwargs.json:
                kwargs.json = addict.Dict()

            kwargs.json.context.client.update(context)

        response = super().request(*args, **kwargs)

        if not response.ok:
            raise errors.InnerTubeException.from_response(response) from None

        data = addict.Dict(response.json())

        if (visitor_data := data.responseContext.visitorData):
            self.headers[enums.Header.VISITOR_ID.value] = visitor_data

        return data
