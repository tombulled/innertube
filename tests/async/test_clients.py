from typing import Optional

import pytest
from innertube import protocols
from innertube.asyncio import clients


@pytest.fixture
def async_adaptor() -> protocols.AsyncAdaptor:
    class FakeAdaptor(protocols.AsyncAdaptor):
        async def dispatch(
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

        async def close(self) -> None:
            return

    return FakeAdaptor()


@pytest.mark.asyncio
async def test_client(async_adaptor: protocols.AsyncAdaptor) -> None:
    client: clients.AsyncClient = clients.AsyncClient(adaptor=async_adaptor)

    assert await client("foo") == {"foo": "bar"}


def test_innertube() -> None:
    with pytest.raises(ValueError):
        clients.InnerTube("FAKE_CLIENT")
