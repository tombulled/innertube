import dataclasses
import http
from typing import Dict, List, Optional

from . import utils


@dataclasses.dataclass
class Locale:
    hl: str
    gl: Optional[str] = None

    def accept_language(self) -> str:
        return ",".join(item for item in (self.hl, self.gl) if item is not None)


@dataclasses.dataclass
class Error:
    code: int
    message: str
    reason: str

    def __str__(self) -> str:
        return f"{self.code} {self.status.phrase}: {self.message}"

    @property
    def status(self) -> http.HTTPStatus:
        return http.HTTPStatus(self.code)


@dataclasses.dataclass
class ClientContext:
    client_name: str
    client_version: str
    client_id: Optional[int] = None
    api_key: Optional[str] = None
    user_agent: Optional[str] = None
    referer: Optional[str] = None
    locale: Optional[Locale] = None

    def params(self) -> Dict[str, str]:
        return utils.filter(
            {
                "key": self.api_key,
                "alt": "json",
            }
        )

    def context(self) -> Dict[str, str]:
        return dict(
            clientName=self.client_name,
            clientVersion=self.client_version,
        )

    def headers(self) -> Dict[str, str]:
        return utils.filter(
            {
                "X-Goog-Api-Format-Version": "1",
                "X-YouTube-Client-Name": str(self.client_id),
                "X-YouTube-Client-Version": self.client_version,
                "User-Agent": self.user_agent,
                "Referer": self.referer,
                "Accept-Language": self.locale and self.locale.accept_language(),
            }
        )


@dataclasses.dataclass
class Config:
    base_url: str
    clients: List[ClientContext]


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


@dataclasses.dataclass
class ResponseFingerprint:
    request: Optional[str] = None
    function: Optional[str] = None
    browse_id: Optional[str] = None
    context: Optional[str] = None
    client: Optional[str] = None
