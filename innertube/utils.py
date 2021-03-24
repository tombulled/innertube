def filter_kwargs(**kwargs) -> dict:
    return \
    {
        key: value
        for key, value in kwargs.items()
        if value is not None
    }

def filter_args(*args) -> list:
    return \
    [
        arg
        for arg in args
        if arg is not None
    ]
