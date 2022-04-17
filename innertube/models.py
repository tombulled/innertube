import dataclasses
import http
import http.client
from typing import Dict, Iterable, Optional, Set

import addict
import furl
import httpx
import parse
from typing_extensions import Self

from . import enums


@dataclasses.dataclass
class Service:
    url: str


@dataclasses.dataclass
class Platform:
    user_agent: str


@dataclasses.dataclass
class Locale:
    hl: str
    gl: Optional[str] = None

    def accept_language(self) -> str:
        return ",".join(item for item in (self.hl, self.gl) if item is not None)


@dataclasses.dataclass
class Client:
    name: str
    version: str
    key: Optional[str] = None


@dataclasses.dataclass
class Context:
    client: Client
    platform: Optional[Platform] = None
    service: Optional[Service] = None
    locale: Optional[Locale] = None

    def prepare(self, session: httpx.Client) -> None:
        session.headers.update(self.headers())
        session.params = session.params.merge(self.params())
        session.context.update(self.context())

    def params(self) -> Dict[str, str]:
        params: Dict[str, str] = {
            "alt": "json",
        }

        if self.client.key is not None:
            params["key"] = self.client.key

        return params

    def context(self) -> Dict[str, str]:
        return dict(
            clientName=self.client.name,
            clientVersion=self.client.version,
        )

    def headers(self) -> Dict[str, str]:
        headers: Dict[str, str] = {
            "X-Goog-Api-Format-Version": '1',
            "X-Goog-Client-Version": self.client.version,
        }

        if self.platform is not None:
            headers["User-Agent"] = self.platform.user_agent

        if self.service is not None:
            headers["Referer"] = self.service.url

        if self.locale is not None:
            headers["Accept-Language"] = self.locale.accept_language()

        return headers


@dataclasses.dataclass
class ResponseContext:
    @dataclasses.dataclass
    class Request:
        type: Optional[str] = None
        id: Optional[str] = None

    @dataclasses.dataclass
    class Client:
        name: Optional[str] = None
        version: Optional[str] = None

    @dataclasses.dataclass
    class Flags:
        logged_in: Optional[bool] = None

    function: Optional[str] = None
    browse_id: Optional[str] = None
    context: Optional[str] = None
    visitor_data: Optional[str] = None
    client: Client = dataclasses.field(default_factory=Client)
    request: Request = dataclasses.field(default_factory=Request)
    flags: Flags = dataclasses.field(default_factory=Flags)

    @classmethod
    def parse(cls, response_context: addict.Dict) -> Self:
        services: addict.Dict = addict.Dict()

        tracker: addict.Dict
        for tracker in response_context.serviceTrackingParams:
            param: addict.Dict
            for param in tracker.params:
                services[tracker.service][param.key] = param.value

        request_type: Optional[str] = None
        request_id: Optional[str] = None

        key: str
        val: str
        for key, val in services.CSI.items():
            result: Optional[parse.Result]
            if result := parse.parse("Get{id}_rid", key):
                named: addict.Dict = addict.Dict(result.named)

                request_type = named.id
                request_id = val

        return cls(
            function=services.CSI.yt_fn or None,
            browse_id=services.GFEEDBACK.browse_id or None,
            context=services.GFEEDBACK.context or None,
            visitor_data=response_context.visitorData or None,
            request=cls.Request(
                type=request_type or None,
                id=request_id or None,
            ),
            client=cls.Client(
                name=services.CSI.c or None,
                version=services.CSI.cver or None,
            ),
            flags=cls.Flags(
                logged_in=(value := services.GFEEDBACK.logged_in or None)
                and bool(int(value)),
            ),
        )

    @classmethod
    def from_response(cls, response: httpx.Response) -> Optional[Self]:
        response_data: addict.Dict = addict.Dict(response.json())

        response_context: Optional[Self] = None

        context: addict.Dict
        if context := response_data.responseContext:
            response_context = cls.parse(context)

        return response_context


@dataclasses.dataclass
class ResponseFingerprint:
    endpoint: Optional[str] = None
    request: Optional[str] = None
    function: Optional[str] = None
    browse_id: Optional[str] = None
    context: Optional[str] = None
    client: Optional[str] = None

    @classmethod
    def from_response(cls, response: httpx.Response, /) -> Self:
        context: Optional[ResponseContext] = ResponseContext.from_response(response)

        return cls(
            endpoint="/".join(furl.furl(response.url).path.segments[2:]),
            request=context.request.type if context is not None else None,
            function=context.function if context is not None else None,
            browse_id=context.browse_id if context is not None else None,
            context=context.context if context is not None else None,
            client=context.client.name if context is not None else None,
        )


@dataclasses.dataclass
class Parser:
    endpoint: Set[str] = dataclasses.field(default_factory=set)
    request: Set[str] = dataclasses.field(default_factory=set)
    function: Set[str] = dataclasses.field(default_factory=set)
    browse_id: Set[str] = dataclasses.field(default_factory=set)
    context: Set[str] = dataclasses.field(default_factory=set)
    client: Set[str] = dataclasses.field(default_factory=set)

    @classmethod
    def from_response_fingerprints(
        cls, *response_fingerprints: ResponseFingerprint
    ) -> Self:
        parser: Self = cls()

        response_fingerprint: ResponseFingerprint
        for response_fingerprint in response_fingerprints:
            key: str
            value: str
            for key, value in dataclasses.asdict(response_fingerprint).items():
                if value is not None:
                    getattr(parser, key).add(value)

        return parser

    def keys(self) -> Iterable[str]:
        return dataclasses.asdict(self).keys()

    def values(self) -> Iterable[str]:
        return dataclasses.asdict(self).values()

    def any(self) -> bool:
        return any(self.values())

    def all(self) -> bool:
        return all(self.values())

    def intersect(self, rhs: Self) -> Self:
        parser: Self = type(self)()

        key: str
        value: str
        for key, value in dataclasses.asdict(self).items():
            if value in getattr(rhs, key):
                getattr(parser, key).add(value)

        return parser

    def union(self, rhs: Self) -> Self:
        parser: Self = type(self)()

        child: Self
        for child in (self, rhs):
            key: str
            value: str
            for key, value in dataclasses.asdict(child).items():
                getattr(parser, key).add(value)

        return parser


@dataclasses.dataclass
class Error:
    code: int
    message: str

    def __str__(self) -> str:
        return f"{self.code} {self.reason}" + (
            f": {self.message}" if self.message else ""
        )

    @property
    def reason(self) -> str:
        return http.client.responses[self.code]

    @property
    def phrase(self) -> str:
        return self.status.phrase

    @property
    def description(self) -> str:
        return self.status.description

    @property
    def status(self) -> http.HTTPStatus:
        return http.HTTPStatus(self.code)

    @classmethod
    def from_response(cls, response: httpx.Response) -> Self:
        return cls(
            code=response.status_code,
            message=f"{response.request.method} {response.url}",
        )


@dataclasses.dataclass
class InnerTubeError(Error):
    status: enums.ErrorStatus
