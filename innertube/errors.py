import dataclasses
import http.client

from . import models


@dataclasses.dataclass
class RequestError(http.client.HTTPException):
    error: models.Error

    def __str__(self) -> str:
        return str(self.error)


class ResponseError(Exception):
    pass


class NoParserFound(Exception):
    pass
