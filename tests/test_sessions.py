import pytest
from innertube.sessions import BaseSession, JSONSession, InnerTubeSession
from innertube.errors import RequestError, ResponseError


def test_base_session() -> None:
    session: BaseSession = BaseSession(base_url="https://foo.com/")

    assert repr(session) == "BaseSession(base_url='https://foo.com/')"


def test_json_session() -> None:
    session: JSONSession = JSONSession(base_url="https://httpbin.org/")

    with pytest.raises(RequestError):
        session.get("status/400")

    with pytest.raises(ResponseError):
        session.get("html")

    session.get("json")


def test_innertube_session() -> None:
    session: InnerTubeSession = InnerTubeSession(
        context={"clientName": "WEB_REMIX", "clientVersion": "0.1"}
    )

    with pytest.raises(RequestError):
        session.post("browse", json={"browseId": "not_a_real_browse_id"})

    session.post("guide")
