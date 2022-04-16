from typing import Any, Iterable, Mapping, Optional, Union

import addict


def filter(
    item: Optional[Union[Mapping, Iterable]] = None, **kwargs: Any
) -> addict.Dict:
    dictionary: dict = dict(item) if item is not None else kwargs

    return addict.Dict(
        {
            key: value
            for key, value in dictionary.items()
            if value is not None and (not isinstance(value, addict.Dict) or value)
        }
    )
