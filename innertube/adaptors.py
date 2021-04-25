import attr
import addict
import furl
import requests
import pydantic

import register

import abc
import typing
import functools

from . import sessions
from . import models
from . import parsers
from . import enums

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class Adaptor(sessions.Session):
    def __call__(self, *args, **kwargs) -> typing.Union[dict, list]:
        return self.get(*args, **kwargs)

@attrs
class JSONAdaptor(Adaptor):
    def send(self, *args, **kwargs) -> typing.Union[dict, list]:
        return super().send(*args, **kwargs).json()

@attrs
class SuggestQueriesAdaptor(JSONAdaptor, sessions.SuggestQueriesSession): pass

@attrs
class BaseInnerTubeAdaptor(Adaptor, sessions.InnerTubeSession):
    def __call__(self, *args, **kwargs) -> models.Response:
        return self.post(*args, **kwargs)

    def send(self, *args, **kwargs) -> models.Response:
        response: requests.Response = super().send(*args, **kwargs)

        response_data: addict.Dict = addict.Dict(response.json())

        response_context: models.ResponseContext = parsers.response_context(response_data.responseContext)

        return models.Response \
        (
            endpoint = '/'.join(furl.furl(response.url).path.segments[2:]),
            context  = response_context,
            data     = response_data,
        )

@attrs
class InnerTubeAdaptor(BaseInnerTubeAdaptor):
    parsers: register.HookedRegister = attr.ib \
    (
        default = attr.Factory \
        (
            functools.partial \
            (
                register.HookedRegister,
                models.Parser,
            )
        ),
        repr = False,
        init = False,
    )

    def __attrs_post_init__(self):
        self.parsers()(lambda data: data)

    def __call__(self, *args, **kwargs) -> typing.Any:
        response: models.Response = super().__call__(*args, **kwargs)

        response_fingerprint: models.ResponseFingerprint = response.fingerprint()

        response_schema = models.Parser.from_model(response_fingerprint)

        for parser, schema in reversed(self.parsers.items()):
            if not schema.any() or (schema & response_schema).any():
                return parser(response.data)

        # TODO: Raise appropriate exception
        raise Exception(f'No parser found for context: {response_context!s}')
