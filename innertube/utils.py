'''
Library containing general utility functions

Usage:
    >>> from innertube import utils
    >>>
    >>> dir(utils)
    ...
    >>>
    >>> utils.url
    <function url at 0x7fd546a173a0>
    >>>
'''

import urllib.parse

from typing import \
(
    Optional,
    Callable,
    Iterable,
    Dict,
    Any,
)

def repr(class_name: str, fields: Dict[str, Any] = None):
    return '{class_name}({fields})'.format \
    (
        class_name = class_name,
        fields     = ', '.join \
        (
            f'{key}={value!r}'
            for key, value in (fields.items() if fields else ())
        )
    )

def url \
        (
            *,
            domain:   str,
            scheme:   str                      = 'https',
            port:     Optional[int]            = None,
            endpoint: Optional[str]            = None,
            params:   Optional[Dict[str, Any]] = None,
        ):
    '''
    Construct a URL

    Args:
        domain: Domain name
            Example: 'google.com'
        scheme:  Request scheme
            Example: 'http'
        port: Request port
            Example: 8080
        endpoint: URI endpoint
            Example: 'api/v1/users'
        params: Query string parameters
            Example: {'username': 'admin', 'password': 'Password1'}

    Returns:
        A constructed URL

    Example:
        >>> url \
        (
            domain   = 'www.google.com',
            scheme   = 'https',
            endpoint = 'search',
            params   = {'q': 'test'},
        )
        'https://www.google.com/search?q=test'
        >>>
    '''

    return '{scheme}://{domain}{sep_port}{port}/{endpoint}{sep_params}{params}'.format \
    (
        scheme     = scheme,
        domain     = domain,
        sep_port   = ':' if port else '',
        port       = port or '',
        endpoint   = endpoint.lstrip(r'\/') if endpoint else '',
        sep_params = '?' if params else '',
        params     = urllib.parse.urlencode(params) if params else '',
    )

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
