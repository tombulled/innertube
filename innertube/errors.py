import addict
import attr
import bs4
import requests

import mime

import http.client
import html.parser

from . import enums
from . import models

@attr.s
class RequestError(Exception):
    error: models.Error = attr.ib()

    def __str__(self) -> str:
        return str(self.error)

    @classmethod
    def from_response(cls, response: requests.Response):
        content_type = response.headers.get(enums.Header.CONTENT_TYPE.value).lower()

        mime_type = mime.parse(content_type)

        error = addict.Dict \
        (
            code    = response.status_code,
            status  = response.reason,
            message = http.client.responses[response.status_code],
        )

        if mime_type.subtype == enums.MediaSubtype.JSON:
            data = addict.Dict(response.json())

            if (error := data.error):
                return cls(models.Error.parse_obj(error))
        elif mime_type.subtype == enums.MediaSubtype.HTML:
            soup = bs4.BeautifulSoup(response.text, html.parser.__name__)

            if (tag := soup.p.p):
                error.message = tag.text

        return cls(models.Error.parse_obj(error))
