import addict

def filter(*args, **kwargs) -> addict.Dict:
    return addict.Dict \
    (
        {
            key: value
            for key, value in dict(*args, **kwargs).items()
            if value is not None \
                and (not isinstance(value, addict.Dict) or value)
        }
    )
