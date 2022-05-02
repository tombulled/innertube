import http

from innertube import models


def test_locale() -> None:
    locale: models.Locale = models.Locale("en", "GB")

    assert locale.accept_language() == "en,GB"


def test_error() -> None:
    error: models.Error = models.Error(
        code=400, message="Precondition check failed.", reason="FAILED_PRECONDITION"
    )

    assert str(error) == "400 Bad Request: Precondition check failed."
    assert error.status == http.HTTPStatus(400)


def test_client_context() -> None:
    client_context: models.ClientContext = models.ClientContext(
        client_name="FAKE_CLIENT",
        client_version="1.0",
        client_id=123,
        api_key="fake_api_key",
        user_agent="FakeUserAgent/1.0",
        referer="https://fake.referer.com/",
        locale=models.Locale("en", "GB"),
    )

    assert client_context.params() == {"key": "fake_api_key", "alt": "json"}
    assert client_context.context() == {
        "clientName": "FAKE_CLIENT",
        "clientVersion": "1.0",
    }
    assert client_context.headers() == {
        "X-Goog-Api-Format-Version": "1",
        "X-YouTube-Client-Name": "123",
        "X-YouTube-Client-Version": "1.0",
        "User-Agent": "FakeUserAgent/1.0",
        "Referer": "https://fake.referer.com/",
        "Accept-Language": models.Locale("en", "GB").accept_language(),
    }
