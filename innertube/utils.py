import benedict
import builtins

def filter(*args, **kwargs):
    if args:
        return list \
        (
            builtins.filter \
            (
                lambda value: value is not None,
                args,
            )
        )

    return benedict.benedict.filter \
    (
        kwargs,
        lambda key, value: value is not None,
    )
