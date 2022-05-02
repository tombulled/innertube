from typing import Optional

import pytest
from innertube import clients, protocols


@pytest.fixture
def adaptor() -> protocols.Adaptor:
    class FakeAdaptor(protocols.Adaptor):
        def dispatch(
            self,
            endpoint: str,
            *,
            params: Optional[dict] = None,
            body: Optional[dict] = None
        ) -> dict:
            return {
                "responseContext": {},
                "foo": "bar",
            }

    return FakeAdaptor()


def test_client(adaptor: protocols.Adaptor) -> None:
    client: clients.Client = clients.Client(adaptor=adaptor)

    assert client("foo") == {"foo": "bar"}


def test_innertube() -> None:
    with pytest.raises(ValueError):
        clients.InnerTube("FAKE_CLIENT")
