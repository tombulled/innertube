from typing import Optional, Protocol, runtime_checkable


@runtime_checkable
class Adaptor(Protocol):
    def dispatch(
        self,
        endpoint: str,
        *,
        params: Optional[dict] = None,
        body: Optional[dict] = None
    ) -> dict:
        raise NotImplementedError
