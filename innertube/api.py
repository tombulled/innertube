import re
from typing import Optional

from . import models
from .config import config
from .models import ClientContext, ResponseContext


def get_context(client_name: str, /) -> Optional[ClientContext]:
    context: ClientContext
    for context in config.clients:
        if context.client_name.upper() == client_name.upper():
            return context

    return None


def fingerprint(data: dict, /) -> Optional[models.ResponseFingerprint]:
    response_context: Optional[ResponseContext] = get_response_context(data)

    if response_context is None:
        return None

    return models.ResponseFingerprint(
        request=response_context.request.type or None,
        function=response_context.function or None,
        browse_id=response_context.browse_id or None,
        context=response_context.context or None,
        client=response_context.client.name or None,
    )


def get_response_context(data: dict, /) -> Optional[ResponseContext]:
    response_context: Optional[dict] = data.get("responseContext")

    if response_context is None:
        return None

    services: dict = {}

    tracker: dict
    for tracker in response_context.get("serviceTrackingParams", ()):
        param: dict
        for param in tracker.get("params", ()):
            services.setdefault(tracker["service"], {})[param["key"]] = param["value"]

    request_type: Optional[str] = None
    request_id: Optional[str] = None

    key: str
    value: str
    for key, value in services.get("CSI", {}).items():
        match: Optional[re.Match] = re.match(r"Get(.+)_rid", key)

        if match is not None:
            request_type = match.group(1)
            request_id = value

    return ResponseContext(
        function=services.get("CSI", {}).get("yt_fn"),
        browse_id=services.get("GFEEDBACK", {}).get("browse_id"),
        context=services.get("GFEEDBACK", {}).get("context"),
        visitor_data=response_context.get("visitorData"),
        request=ResponseContext.Request(
            type=request_type,
            id=request_id,
        ),
        client=ResponseContext.Client(
            name=services.get("CSI", {}).get("c"),
            version=services.get("CSI", {}).get("cver"),
        ),
        flags=ResponseContext.Flags(
            logged_in=(value := services.get("GFEEDBACK", {}).get("logged_in"))
            and bool(int(value)),
        ),
    )


def error(error: dict, /) -> models.Error:
    return models.Error(
        code=error["code"], message=error["message"], reason=error["status"]
    )


def contextualise(client_context: ClientContext, data: dict) -> dict:
    data.setdefault("context", {}).setdefault("client", {}).update(
        client_context.context()
    )

    return data
