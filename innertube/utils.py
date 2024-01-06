import re
from typing import Any, Mapping, Sequence


def filter(dictionary: dict, /) -> dict:
    return {key: value for key, value in dictionary.items() if value is not None}

def is_renderable(data: Any, /) -> bool:
    """
    >>> is_renderable({"FooRenderer": {}})
    True
    >>> is_renderable({})
    False
    """

    # print("is_renderable", data)

    if isinstance(data, Sequence):
        return all(map(is_renderable, data))

    if not isinstance(data, Mapping):
        return False
    
    if len(data) != 1:
        return False
    
    key: Any = next(iter(data))
    value: Any = data[key]

    if not isinstance(key, str):
        return False
    
    if not re.match(r"(.+)Renderer", key):
        return False
    
    if not isinstance(value, Mapping):
        return False
    
    return True