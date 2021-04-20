import parse
import addict

# from . import types
from . import models
from . import utils

def response_context(response_context: addict.Dict) -> models.ResponseContext:
    services = addict.Dict()

    for tracker in response_context.serviceTrackingParams:
        for param in tracker.params:
            services[tracker.service][param.key] = param.value

    request_type = None
    request_id   = None

    for key, val in services.CSI.items():
        if (result := parse.parse('Get{id}_rid', key)):
            result = addict.Dict(result.named)

            request_type = result.id
            request_id   = val

    context = utils.filter \
    (
        request = utils.filter \
        (
            type = request_type,
            id   = request_id,
        ),
        function  = services.CSI.yt_fn,
        browse_id = services.GFEEDBACK.browse_id,
        context   = services.GFEEDBACK.context,
        client    = utils.filter \
        (
            name    = services.CSI.c,
            version = services.CSI.cver,
        ),
        visitor_data = response_context.visitorData,
        flags = utils.filter \
        (
            logged_in = (value := services.GFEEDBACK.logged_in) and bool(int(value)),
        ),
    )

    return models.ResponseContext.parse_obj(context)
