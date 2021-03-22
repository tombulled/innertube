'''
Library containing general utility functions

Usage:
    >>> from innertube import utils
    >>>
    >>> dir(utils)
    ...
    >>>
'''

def filtered_dict(**dictionary) -> dict:
    return \
    {
        key: val
        for key, val in dictionary.items()
        if val is not None
    }

def filtered_list(*items) -> list:
    return \
    [
        item
        for item in items
        if item is not None
    ]
