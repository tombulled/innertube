import fastapi
import httpx
import innertube
import pytest
from innertube.errors import RequestError, ResponseError
from innertube.asyncio.adaptor import AsyncInnerTubeAdaptor


@pytest.fixture
def app() -> fastapi.FastAPI:
    app = fastapi.FastAPI()

    @app.post("/good")
    def good():
        return fastapi.responses.JSONResponse(
            {"responseContext": {}, "configData": "", "globalConfig": {}}
        )

    @app.post("/error")
    def error():
        return fastapi.responses.JSONResponse(
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
        headers = {"Content-Type": "application/text"}
        return fastapi.responses.Response("foo", headers=headers)

    return app


@pytest.fixture
def async_adaptor(app: fastapi.FastAPI) -> AsyncInnerTubeAdaptor:
    return AsyncInnerTubeAdaptor(
        context=innertube.ClientContext("FAKE_CLIENT", "1.0"),
        session=httpx.AsyncClient(app=app, base_url="https://foo.bar/"),
    )


@pytest.mark.asyncio
async def test_good_response(event_loop, async_adaptor: AsyncInnerTubeAdaptor) -> None:
    response = await async_adaptor.dispatch("/good")
    assert isinstance(response, dict)


@pytest.mark.asyncio
async def test_error(async_adaptor: AsyncInnerTubeAdaptor) -> None:
    with pytest.raises(RequestError):
        await async_adaptor.dispatch("/error")


@pytest.mark.asyncio
async def test_bad_response(async_adaptor: AsyncInnerTubeAdaptor) -> None:
    with pytest.raises(ResponseError):
        await async_adaptor.dispatch("/bad")
