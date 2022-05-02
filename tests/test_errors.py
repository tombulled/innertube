from innertube.errors import RequestError
from innertube.models import Error


def test_request_error() -> None:
    exception: RequestError = RequestError(
        error=Error(
            code=400, message="Precondition check failed.", reason="FAILED_PRECONDITION"
        )
    )

    assert str(exception) == "400 Bad Request: Precondition check failed."
