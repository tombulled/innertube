from typing import Union

def url(*, domain: str, scheme: str = 'https', port: Union[int, None] = None, endpoint: Union[str, None] = None):
    return '{scheme}://{domain}{sep_port}{port}/{endpoint}'.format \
    (
        scheme   = scheme,
        domain   = domain,
        sep_port = ':' if port else '',
        port     = port or '',
        endpoint = endpoint.lstrip(r'\/') if endpoint else '',
    )

'''
Module containing the utility function: filter
'''

from typing import Callable, Iterable

def filter \
        (
            iterable: Iterable,
            func:     Callable = None,
        ) -> Iterable:
    '''
    Filter an iterable.

    Return an iterable containing those items of iterable for which func(item),
    or func(key, value) if the iterable is a dict, are true.

    Args:
        iterable: An iterable to filter
        func: A function to filter items by
            Note: If the iterable *is* a dictionary, the function signature
                is func(key: Any, value: Any) -> bool
            Note: If the iterable is *not* a dictionary, the function signature
                is func(item: Any) -> bool
    Returns:
        If isinstance(iterable, dict):
            Returns dict
        Else:
            Returns list
    Example:
        If isinstance(iterable, dict):
            >>> data = {'a': 1, 'b': None, 'c': 3}
            >>> filter(data)
            {'a': 1, 'c': 3}
            >>>
        Else:
            >>> data = [1, None, 3]
            >>> filter(data)
            [1, 3]
            >>>
    '''

    if isinstance(iterable, dict):
        if not func:
            func = lambda key, val: val is not None

        return \
        {
            key: val
            for key, val in iterable.items()
            if func(key, val)
        }
    else:
        if func is None:
            func = lambda item: item is not None

        return \
        [
            val
            for val in iterable
            if func(val)
        ]
