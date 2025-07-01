import innertube.utils


def test_filter() -> None:
    assert innertube.utils.filter({"a": None, "b": "b", "c": "c"}) == {"b": "b", "c": "c"}
