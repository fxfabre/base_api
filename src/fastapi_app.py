import logging
from collections.abc import Awaitable
from typing import Callable

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi_utils.timing import add_timing_middleware
from pyinstrument import Profiler
from starlette.responses import JSONResponse, RedirectResponse, Response

from src.controllers import router
from src.controllers.healthcheck import healthcheck_router

logger = logging.getLogger(__name__)

app = FastAPI(
    title="Project title",
    version="1.0",
    description="Project description",
    default_response_class=JSONResponse,
    on_startup=[
        # Put here a Callable to do some heavy loading, like cache loading
        lambda: logger.info("FastAPI ready")
    ],
)
add_timing_middleware(app, record=logger.info, prefix="app")
app.include_router(router, prefix="/api/v1")
app.include_router(healthcheck_router, prefix="/healthcheck")


@app.middleware("http")
async def add_process_time_header(
    request: Request, call_next: Callable[[Request], Awaitable[Response]]
) -> Response:
    logger.debug("Request on %s", request.url)
    return await call_next(request)


@app.middleware("http")
async def profile_request(request: Request, call_next) -> Response:
    if request.headers.get("X-profiling", False):
        profiler = Profiler(interval = 0.001)
        profiler.start()
        response = await call_next(request)
        profiler.stop()
        return HTMLResponse(profiler.output_html())
    else:
        return await call_next(request)


@app.get("/", include_in_schema=False)
async def docs_redirect() -> RedirectResponse:
    return RedirectResponse(url="/docs", status_code=302)


@app.exception_handler(Exception)
async def http_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.error("Error during request %s", request.url, exc_info=exc)
    return JSONResponse(
        {
            "Type": type(exc).__name__,
            "Error": str(exc.args),
        },
        status_code=500,
    )
