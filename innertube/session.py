import attr
import addict
import requests_toolbelt.sessions

import functools

from . import errors
from . import enums
from . import models


@attr.s(init = False)
class Session(requests_toolbelt.sessions.BaseUrlSession):
    base_url: str = attr.ib()
    
    __info: models.AdaptorInfo

    def __init__(self, info: models.AdaptorInfo):
        super().__init__(base_url = info.base_url)

        self.headers.update(info.headers.dump())
        self.params.update(info.params.dump())

        self.__info = info

    @functools.wraps(requests_toolbelt.sessions.BaseUrlSession.request)
    def request(self, *args, **kwargs) -> addict.Dict:
        kwargs = addict.Dict(kwargs)

        if not kwargs.json:
            kwargs.json = addict.Dict()

        kwargs.json.context.client.update(self.__info.context.dump())

        response = super().request(*args, **kwargs)

        if not response.ok:
            raise errors.InnerTubeException.from_response(response) from None

        data = addict.Dict(response.json())

        if (visitor_data := data.responseContext.visitorData):
            self.headers[enums.Header.VISITOR_ID.value] = visitor_data

        return data
