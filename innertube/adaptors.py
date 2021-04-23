import attr
import addict
import furl
import requests

import register

import abc
import typing
import functools

from . import sessions
from . import models
from . import parsers

attrs = attr.s \
(
    auto_detect  = True,
    auto_attribs = True,
)

@attrs
class Adaptor(object):
    session: sessions.Session = attr.ib \
    (
        default = attr.Factory(sessions.Session),
    )

    def __call__(self, *args, **kwargs) -> typing.Union[dict, list]:
        return self.get(*args, **kwargs)

    def get(self, *args, **kwargs) -> typing.Union[dict, list]:
        return self.session.get(*args, **kwargs).json()

    def post(self, *args, **kwargs) -> typing.Union[dict, list]:
        return self.session.post(*args, **kwargs).json()

@attrs
class BaseSuggestQueriesAdaptor(Adaptor):
    session: sessions.SuggestQueriesSession = attr.ib \
    (
        default = attr.Factory(sessions.SuggestQueriesSession),
    )

@attrs
class BaseInnerTubeAdaptor(Adaptor):
    session: sessions.InnerTubeSession = attr.ib \
    (
        default = attr.Factory(sessions.InnerTubeSession),
    )

    def __call__(self, *args, **kwargs) -> addict.Dict:
        return addict.Dict(self.post(*args, **kwargs))

@attrs
class SuggestQueriesAdaptor(BaseSuggestQueriesAdaptor): pass

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

    def __call__(self, *args, **kwargs):
        response = self.session.post(*args, **kwargs)

        response_data = addict.Dict(response.json())

        response_context: models.ResponseContext = parsers.response_context(response_data.responseContext)

        response_fingerprint: models.ResponseFingerprint = models.ResponseFingerprint \
        (
            request   = response_context.request.type,
            function  = response_context.function,
            browse_id = response_context.browse_id,
            context   = response_context.context,
            client    = response_context.client.name,
            endpoint  = '/'.join(furl.furl(response.url).path.segments[2:]),
        )

        response_schema = models.Parser.from_model(response_fingerprint)

        for parser, schema in reversed(self.parsers.items()):
            if not schema.any() or (schema & response_schema).any():
                return parser(response_data)

        # TODO: Raise appropriate exception
        raise Exception(f'No parser found for context: {response_context!s}')
