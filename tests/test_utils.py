import innertube.utils
import addict


def test_filter() -> None:
    assert innertube.utils.filter(
        (("a", None), ("b", addict.Dict()), ("c", 123))
    ) == addict.Dict(c=123)
    assert innertube.utils.filter(
        {"a": None, "b": addict.Dict(), "c": 123}
    ) == addict.Dict(c=123)
    assert innertube.utils.filter(a=None, b=addict.Dict(), c=123) == addict.Dict(c=123)
