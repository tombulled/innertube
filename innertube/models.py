import dataclasses
import http
import http.client
from typing import Dict, Iterable, List, Optional, Set

import addict
import furl
import httpx
import parse
import ua
from typing_extensions import Self

from . import enums, utils


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
    client: Optional[Client] = dataclasses.field(default_factory=Client)
    request: Optional[Request] = dataclasses.field(default_factory=Request)
    flags: Optional[Flags] = dataclasses.field(default_factory=Flags)

    @classmethod
    def parse(cls, response_context: addict.Dict):
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
                result: addict.Dict = addict.Dict(result.named)

                request_type = result.id
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

        context: addict.Dict
        if context := response_data.responseContext:
            return cls.parse(context)


@dataclasses.dataclass
class ResponseFingerprint:
    endpoint: Optional[str] = None
    request: Optional[str] = None
    function: Optional[str] = None
    browse_id: Optional[str] = None
    context: Optional[str] = None
    client: Optional[str] = None

    @classmethod
    def from_response(cls, response: httpx.Response) -> Self:
        context: ResponseContext = ResponseContext.from_response(response)

        return cls(
            endpoint="/".join(furl.furl(response.url).path.segments[2:]),
            request=context.request.type,
            function=context.function,
            browse_id=context.browse_id,
            context=context.context,
            client=context.client.name,
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
class Locale:
    hl: str
    gl: Optional[str] = None

    def accept_language(self) -> str:
        return ",".join(item for item in (self.hl, self.gl) if item is not None)


@dataclasses.dataclass
class Error:
    code: http.HTTPStatus
    message: str

    def __repr__(self) -> str:
        return f"<Error [{self.code} {self.reason}]>"

    def __str__(self) -> str:
        return f"{self.code} {self.reason}" + (
            f": {self.message}" if self.message else ""
        )

    @property
    def reason(self) -> str:
        return http.client.responses[self.code]

    @classmethod
    def from_response(cls, response: httpx.Response) -> Self:
        return cls(
            code=response.status_code,
            message=f"{response.request.method} {response.url}",
        )


@dataclasses.dataclass
class InnerTubeError(Error):
    status: enums.ErrorStatus


@dataclasses.dataclass
class Adaptor:
    params: dict
    headers: dict
    context: dict


@dataclasses.dataclass
class Host:
    domain: str
    scheme: str = enums.Scheme.HTTPS
    port: Optional[int] = None

    def __str__(self) -> str:
        return str(self.url())

    def url(self) -> furl.furl:
        return furl.furl(
            scheme=self.scheme,
            host=self.domain,
            port=self.port,
            path="/",
        )


@dataclasses.dataclass
class Api(Host):
    mount: str = "/"

    def __str__(self) -> str:
        return str(self.url() / self.mount)


@dataclasses.dataclass
class DeviceInfo:
    identifier: str
    family: enums.DeviceFamily
    comments: List[str]

    def product(self) -> Optional[ua.Product]:
        if self.family == enums.DeviceFamily.WEB:
            return ua.Product(
                name=enums.Product.MOZILLA.value,
                version=enums.Product.MOZILLA.version,
                comments=self.comments,
            )


@dataclasses.dataclass
class ServiceInfo:
    domain: str

    def host(self) -> Host:
        return Host(
            domain=self.domain,
        )


@dataclasses.dataclass
class ClientInfo:
    name: str
    version: str
    key: str
    id: Optional[int] = None
    project: Optional[str] = None
    client: Optional[str] = None
    screen: Optional[str] = None

    def params(self) -> dict:
        return dict(
            key=self.key,
            alt=enums.Alt.JSON.value,
        )

    def context(self, locale: Optional[Locale] = None) -> Dict[str, str]:
        return dict(
            clientName=self.name,
            clientVersion=self.version,
            **(locale.dict() if locale else {}),
        )


@dataclasses.dataclass
class ClientSchema:
    client: enums.Client
    device: enums.Device
    service: enums.Service


@dataclasses.dataclass
class Client:
    client: ClientInfo
    device: DeviceInfo
    service: ServiceInfo

    def package(self) -> Optional[str]:
        if self.client.project:
            return ".".join(
                (
                    enums.Domain.GOOGLE.reverse(),
                    self.device.identifier,
                    self.client.project,
                ),
            )

    def product(self) -> ua.Product:
        package: Optional[str] = self.package()

        if package is None:
            return self.device.product()

        return ua.Product(
            name=package, version=self.client.version, comments=self.device.comments
        )

    def headers(self, locale: Optional[Locale] = None) -> Dict[str, str]:
        return utils.filter(
            {
                str(enums.YouTubeHeader.CLIENT_NAME): self.client.id
                and str(self.client.id),
                str(enums.YouTubeHeader.CLIENT_VERSION): self.client.version,
                str(enums.Header.USER_AGENT): str(self.product()),
                str(enums.Header.REFERER): str(self.service.host()),
                str(enums.Header.ACCEPT_LANGUAGE): locale and locale.accept_language(),
            }
        )

    def adaptor(self, locale: Optional[Locale] = None) -> Adaptor:
        return Adaptor(
            params=self.client.params(),
            context=self.client.context(locale=locale),
            headers=self.headers(locale=locale),
        )
