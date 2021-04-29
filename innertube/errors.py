import attr
import pydantic

import http.client

from . import models

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class ModelException(Exception):
    model: pydantic.BaseModel

    def __str__(self) -> str:
        return str(self.model)

@attrs
class RequestError(ModelException, http.client.HTTPException):
    model: models.Error

@attrs
class ResponseError(Exception): pass

@attrs
class NoParserFound(Exception): pass
