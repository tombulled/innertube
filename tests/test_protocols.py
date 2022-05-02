from typing import Optional

from innertube.protocols import Adaptor


def test_not_adaptor() -> None:
    class Foo:
        pass

    assert not isinstance(Foo, Adaptor)


def test_adaptor() -> None:
    class Foo:
        def dispatch(
            self,
            endpoint: str,
            *,
            params: Optional[dict] = None,
            body: Optional[dict] = None
        ) -> dict:
            raise NotImplementedError

    assert isinstance(Foo, Adaptor)
