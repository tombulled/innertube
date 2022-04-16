from innertube.errors import RequestError
from innertube.models import Error


def test_request_error() -> None:
    error: Error = Error(code=400, message="Request contains an invalid argument.")

    exception: RequestError = RequestError(error)

    assert str(exception) == "400 Bad Request: Request contains an invalid argument."
