from . import clients, config
from .models import Context, Locale


class InnerTube(clients.InnerTubeClient):
    locale: Locale

    def __init__(
        self,
        client_name: str,
        locale: Locale = Locale("en", "GB"),
    ):
        super().__init__()

        identifier: str = client_name.lower()

        if identifier not in config.contexts:
            raise ValueError(f"Unrecognised client {client_name!r}")

        self.locale = locale
        context: Context = config.contexts[identifier]

        self.session.headers.update(context.headers())
        self.session.params = self.session.params.merge(context.params())
        self.session.context.update(context.context())

    def __repr__(self) -> str:
        return f"{type(self).__name__}({self.context.client.name!r})"
