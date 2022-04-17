from typing import Optional

from . import clients
from .models import Client, Context, Locale, Platform, Service


class InnerTube(clients.InnerTubeClient):
    def __init__(
        self,
        client_name: str,
        client_version: str,
        *,
        api_key: Optional[str] = None,
        user_agent: Optional[str] = None,
        referer: Optional[str] = None,
        locale: Optional[Locale] = None,
    ):
        super().__init__()

        context: Context = Context(
            client=Client(name=client_name, version=client_version, key=api_key),
            platform=(
                Platform(user_agent=user_agent) if user_agent is not None else None
            ),
            service=(Service(url=referer) if referer is not None else None),
            locale=locale,
        )

        context.prepare(self.session)

    def __repr__(self) -> str:
        return "{cls}({client_name!r}, {client_version!r})".format(
            cls=type(self).__name__,
            client_name=self.session.context["clientName"],
            client_version=self.session.context["clientVersion"],
        )
