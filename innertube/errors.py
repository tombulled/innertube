import dataclasses

from . import models


@dataclasses.dataclass
class RequestError(Exception):
    error: models.Error

    def __str__(self) -> str:
        return str(self.error)


class ResponseError(Exception):
    pass
