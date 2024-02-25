from typing import Any, Mapping, Optional, Sequence, Set, Union
from typing_extensions import TypeAlias
import rich
from pydantic import TypeAdapter
from innertube import InnerTube, utils
from innertube.renderers import parse_renderable
from innertube.raw_models import Response, ResponseContext
from innertube.renderers import RENDERERS

IGNORE_FIELDS: Set[str] = {"responseContext", "trackingParams"}

# response_context: ResponseContext = ResponseContext.model_validate(
#     data["responseContext"]
# )
# tracking_params: str = TypeAdapter(str).validate_python(
#     data.get("trackingParams")
# )

"""
{
    "responseContext": {
        "visitorData": "...",
        "...": "...",
    },
    "items": [
        {
            "SomeRenderer": {
                "...": "...",
            },
            "SomeOtherRenderer": {
                "...": "...",
            },
        }
    ],
    "trackingParams": "CAAQumkiEwiYnZL5osmDAxVOBwYAHQe9Czw="
}
"""


def parse_response(response: dict, /):
    parsed = {}

    key: str
    value: Mapping[str, Any]
    for key, value in response.items():
        if key in IGNORE_FIELDS:
            rich.print(f"{key} -> [IGNORE]")
            # parsed[key] = value
            continue

        parsed[key] = parse_renderable(value)

    return parsed


# Clients
WEB = InnerTube("WEB", "2.20230728.00.00")
WEB_REMIX = InnerTube("WEB_REMIX", "1.20220607.03.01")
IOS = InnerTube("IOS", "17.14.2")
IOS_MUSIC = InnerTube("IOS_MUSIC", "4.16.1")

# Arctic Monkeys
channel_id: str = "UC8Yu1_yfN5qPh601Y4btsYw"

# data_browse_channel = WEB_REMIX.adaptor.dispatch(
#     "browse", body={"browseId": channel_id}
# )
response = WEB_REMIX.adaptor.dispatch("guide")

# rc_1 = ResponseContext.model_validate(data_browse_channel["responseContext"])
# rc_2 = ResponseContext.model_validate(data_guide["responseContext"])

# d = parse(data_browse_channel)
d = parse_response(response)
