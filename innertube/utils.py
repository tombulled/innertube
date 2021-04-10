import typing

def filter(function: typing.Callable[[str, str], bool] = None, **kwargs) -> dict:
    if not function:
        function = lambda key, value: value is not None

    return \
    {
        key: value
        for key, value in kwargs.items()
        if function(key, value)
    }
