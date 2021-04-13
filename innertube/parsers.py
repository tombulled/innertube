import parse

from . import types
from . import models

def response_context(response_context: types.Dict) -> models.ResponseContext:
    services = types.Dict()

    for tracker in response_context.serviceTrackingParams:
        for param in tracker.params:
            services[tracker.service][param.key] = param.value

    request_type = None
    request_id   = None

    for key, val in services.CSI.items():
        if (result := parse.parse('Get{id}_rid', key)):
            result = types.Dict(result.named)

            request_type = result.id
            request_id   = val

    context = types.Dict \
    (
        request = types.Dict \
        (
            type = request_type,
            id   = request_id,
        ).filter(),
        function  = services.CSI.yt_fn,
        browse_id = services.GFEEDBACK.browse_id,
        context   = services.GFEEDBACK.context,
        client    = types.Dict \
        (
            name    = services.CSI.c,
            version = services.CSI.cver,
        ).filter(),
        visitor_data = response_context.visitorData,
        flags = types.Dict \
        (
            logged_in = (value := services.GFEEDBACK.logged_in) and bool(int(value)),
        ).filter(),
    ).filter()

    return models.ResponseContext.parse_obj(context)
