import http
import http.client
from typing import Dict, List, Optional

import addict
import furl
import httpx
import parse
import pydantic
import soset
import ua
from typing_extensions import Self

from . import enums, utils


class BaseModel(pydantic.BaseModel):
    pass


class ResponseContext(BaseModel):
    class Request(BaseModel):
        type: Optional[str]
        id: Optional[str]

    class Client(BaseModel):
        name: Optional[str]
        version: Optional[str]

    class Flags(BaseModel):
        logged_in: Optional[bool]

    function: Optional[str]
    browse_id: Optional[str]
    context: Optional[str]
    visitor_data: Optional[str]
    client: Optional[Client] = pydantic.Field(default_factory=Client)
    request: Optional[Request] = pydantic.Field(default_factory=Request)
    flags: Optional[Flags] = pydantic.Field(default_factory=Flags)

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

        context: addict.Dict = utils.filter(
            function=services.CSI.yt_fn,
            browse_id=services.GFEEDBACK.browse_id,
            context=services.GFEEDBACK.context,
            visitor_data=response_context.visitorData,
            request=utils.filter(
                type=request_type,
                id=request_id,
            ),
            client=utils.filter(
                name=services.CSI.c,
                version=services.CSI.cver,
            ),
            flags=utils.filter(
                logged_in=(value := services.GFEEDBACK.logged_in) and bool(int(value)),
            ),
        )

        return cls.parse_obj(context)

    @classmethod
    def from_response(cls, response: httpx.Response) -> Optional[Self]:
        response_data: addict.Dict = addict.Dict(response.json())

        context: addict.Dict
        if context := response_data.responseContext:
            return cls.parse(context)


class ResponseFingerprint(BaseModel):
    endpoint: Optional[str]
    request: Optional[str]
    function: Optional[str]
    browse_id: Optional[str]
    context: Optional[str]
    client: Optional[str]

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


class Parser(soset.Sets[ResponseFingerprint]):
    pass


class Locale(BaseModel):
    hl: str
    gl: Optional[str]

    def accept_language(self) -> str:
        return ",".join(item for item in (self.hl, self.gl) if item is not None)


class Error(BaseModel):
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


class InnerTubeError(Error):
    status: enums.ErrorStatus


class Adaptor(BaseModel):
    params: dict
    headers: dict
    context: dict


class Host(BaseModel):
    scheme: str = enums.Scheme.HTTPS
    domain: str
    port: Optional[int]

    def __str__(self) -> str:
        return str(self.url())

    def url(self) -> furl.furl:
        return furl.furl(
            scheme=self.scheme,
            host=self.domain,
            port=self.port,
            path="/",
        )


class Api(Host):
    mount: str = "/"

    def __str__(self) -> str:
        return str(self.url() / self.mount)


class DeviceInfo(BaseModel):
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


class ServiceInfo(BaseModel):
    domain: str

    def host(self) -> Host:
        return Host(
            domain=self.domain,
        )


class ClientInfo(BaseModel):
    name: str
    version: str
    key: str
    id: Optional[int]
    project: Optional[str]
    client: Optional[str]
    screen: Optional[str]

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


class ClientSchema(BaseModel):
    client: enums.Client
    device: enums.Device
    service: enums.Service


class Client(BaseModel):
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
