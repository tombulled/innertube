import functools

from .enums import \
(
    ApiEndpoint,
)

def method(endpoint: ApiEndpoint):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(self, *args, **kwargs):
            if endpoint not in self.info.service.endpoints:
                raise NotImplementedError \
                (
                    'Service {service!r} doesn\'t implement method for endpoint {endpoint!r}'.format \
                    (
                        service  = self.info.service.name,
                        endpoint = endpoint.value,
                    )
                )

            return func \
            (
                functools.partial \
                (
                    self.adaptor.dispatch,
                    endpoint = endpoint.value,
                ),
                *args,
                **kwargs,
            )

        return wrapper

    return decorator
