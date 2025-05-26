import innertube.utils


def test_removeNoneValues() -> None:
    assert innertube.utils.removeNoneValues({"a": None, "b": {}, "c": 123}) == dict(b={}, c=123)
