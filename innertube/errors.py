import attr
import pydantic

import http.client

from . import models

@attr.s
class ModelException(Exception):
    model: pydantic.BaseModel = attr.ib()

    def __str__(self) -> str:
        return str(self.model)

@attr.s
class HttpException(ModelException, http.client.HTTPException):
    model: models.Error = attr.ib()
