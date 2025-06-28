from typing import Dict, Optional, TypeVar

__all__ = ("filter",)

K = TypeVar("K")
V = TypeVar("V")


def filter(dictionary: Dict[K, Optional[V]], /) -> Dict[K, V]:
    return {key: value for key, value in dictionary.items() if value is not None}
