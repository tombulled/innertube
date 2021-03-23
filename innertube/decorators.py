import functools

from .enums import \
(
    Endpoint,
)

def method(endpoint: Endpoint):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            # if endpoint not in self.session.info.service.endpoints:
            #     raise NotImplementedError \
            #     (
            #         'Service {service!r} doesn\'t implement method for endpoint {endpoint!r}'.format \
            #         (
            #             service  = self.session.info.service.name,
            #             endpoint = endpoint.value,
            #         )
            #     )

            return func \
            (
                functools.partial \
                (
                    self.session.post,
                    endpoint.value,
                ),
                *args,
                **kwargs,
            )

        return wrapper

    return decorator
