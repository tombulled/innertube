import flask
import httpx
import innertube
import pytest
from innertube.config import config
from innertube.errors import RequestError, ResponseError


@pytest.fixture
def app() -> flask.Flask:
    app: flask.Flask = flask.Flask(__name__)

    @app.post("/good")
    def good():
        return flask.jsonify(
            {"responseContext": {}, "configData": "", "globalConfig": {}}
        )

    @app.post("/error")
    def error():
        return flask.jsonify(
            {
                "error": {
                    "code": 400,
                    "message": "Invalid value at 'context.client.client_name' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.ClientInfo.ClientName), \"FOO\"",
                    "errors": [
                        {
                            "message": "Invalid value at 'context.client.client_name' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.ClientInfo.ClientName), \"FOO\"",
                            "reason": "invalid",
                        }
                    ],
                    "status": "INVALID_ARGUMENT",
                    "details": [
                        {
                            "@type": "type.googleapis.com/google.rpc.BadRequest",
                            "fieldViolations": [
                                {
                                    "field": "context.client.client_name",
                                    "description": "Invalid value at 'context.client.client_name' (type.googleapis.com/youtube.api.pfiinnertube.YoutubeApiInnertube.ClientInfo.ClientName), \"FOO\"",
                                }
                            ],
                        }
                    ],
                }
            }
        )

    @app.post("/bad")
    def bad():
        return "foo"

    return app


@pytest.fixture
def adaptor(app: flask.Flask) -> innertube.InnerTubeAdaptor:
    return innertube.InnerTubeAdaptor(
        context=innertube.ClientContext("FAKE_CLIENT", "1.0"),
        session=httpx.Client(app=app, base_url="https://foo.bar/"),
    )


def test_good_response(adaptor: innertube.InnerTubeAdaptor) -> None:
    assert isinstance(adaptor.dispatch("/good"), dict)


def test_error(adaptor: innertube.InnerTubeAdaptor) -> None:
    with pytest.raises(RequestError):
        adaptor.dispatch("/error")


def test_bad_response(adaptor: innertube.InnerTubeAdaptor) -> None:
    with pytest.raises(ResponseError):
        adaptor.dispatch("/bad")
