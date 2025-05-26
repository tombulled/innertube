def removeNoneValues(dictionary: dict, /) -> dict:
    """Removes None values from a dictionary."""
    return {key: value for key, value in dictionary.items() if value is not None}


def _find_paths(
    data: dict, key: str = None, value: str = None, current_path: list = None
):
    """
    Walks through a dictionary with nested dictionaries and lists
    and returns all paths to a given key or value.
    """
    if current_path is None:
        current_path = []
    paths = []

    items = data.items() if isinstance(data, dict) else enumerate(data)
    for k, v in items:
        current_path.append(k)

        if (key is not None and k == key) or (value is not None and v == value):
            paths.append(tuple(current_path))

        if isinstance(v, (dict, list)):
            paths.extend(find_paths(v, key, value, current_path))

        current_path.pop()

    return paths


def _path_list_as_python_repr(paths):
    """Turns a list ['a', 0, 'b'] into python index syntax ['a'][0]['b']"""
    return ["".join("[" + repr(k) + "]" for k in i) for i in paths]


def find_paths(data: dict, key: str = None, value: str = None):
    """
    Walks through a dictionary with nested dictionaries and lists
    and returns all paths to a given key or value in python index syntax.
    """
    return _path_list_as_python_repr(_find_paths(data, key, value))
