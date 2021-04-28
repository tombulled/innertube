import parse
import addict

import typing

from . import models
from . import utils

def response_context(response_context: addict.Dict) -> models.ResponseContext:
    services = addict.Dict()

    for tracker in response_context.serviceTrackingParams:
        for param in tracker.params:
            services[tracker.service][param.key] = param.value

    request_type: typing.Optional[str] = None
    request_id:   typing.Optional[str] = None

    for key, val in services.CSI.items():
        if (result := parse.parse('Get{id}_rid', key)):
            result = addict.Dict(result.named)

            request_type = result.id
            request_id   = val

    context = utils.filter \
    (
        function     = services.CSI.yt_fn,
        browse_id    = services.GFEEDBACK.browse_id,
        context      = services.GFEEDBACK.context,
        visitor_data = response_context.visitorData,
        request = utils.filter \
        (
            type = request_type,
            id   = request_id,
        ),
        client = utils.filter \
        (
            name    = services.CSI.c,
            version = services.CSI.cver,
        ),
        flags = utils.filter \
        (
            logged_in = (value := services.GFEEDBACK.logged_in) and bool(int(value)),
        ),
    )

    return models.ResponseContext.parse_obj(context)
