def filter(dictionary: dict, /) -> dict:
    return {key: value for key, value in dictionary.items() if value is not None}
