def filter(function = None, **kwargs) -> dict:
    return \
    {
        key: value
        for key, value in kwargs.items()
        if \
        (
            function(value)
            if function
            else value is not None
        )
    }
