"""Notification microservice - entry point.

Run:  uvicorn app.main:app --reload --port 8084
  or: python -m app.main
"""
import os
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.eureka import start_eureka, stop_eureka
from app.routers import notification

PORT = int(os.getenv("PORT", "8084"))


@asynccontextmanager
async def lifespan(app: FastAPI):
    await start_eureka(PORT)
    try:
        yield
    finally:
        await stop_eureka()


app = FastAPI(
    title="Notification Microservice API",
    version="1.0.0",
    description=(
        "Notification microservice (Python / FastAPI, no database). "
        "Only the hello endpoint is implemented; the notification logic is to be developed by students."
    ),
    contact={"name": "Badia Abouhdid"},
    servers=[{"url": f"http://localhost:{PORT}", "description": "Local"}],
    docs_url="/swagger-ui",
    openapi_url="/v3/api-docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

app.include_router(notification.router)


@app.get("/health", tags=["Observability"])
def health():
    return {"status": "UP"}


@app.get("/info", tags=["Observability"])
def info():
    return {
        "app": {
            "name": "notification",
            "version": "1.0.0",
            "description": "Notification microservice (Python / FastAPI)",
        }
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=True)
