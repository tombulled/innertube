import innertube.utils


def test_filter() -> None:
    assert innertube.utils.filter({"a": None, "b": {}, "c": 123}) == dict(b={}, c=123)
