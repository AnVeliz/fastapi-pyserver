from fastapi import FastAPI
from server.api.public import app_public
from server.api.private import app_private

app = FastAPI(
    title="FastAPI PyServer",
    description="Simple FastAPI Python server.",
    version="0.0.1"
)

app.include_router(
    app_private,
    #prefix="/private",
    dependencies=[],
)
app.include_router(
    app_public,
    #prefix="/public",
    dependencies=[],
)