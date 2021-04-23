from fastapi import FastAPI, Depends
from server.api.public import app_public
from server.api.private import app_private
from server.middleware.access_control import check_token
from server.services.database import generate_database

app = FastAPI(title="FastAPI PyServer", description="Simple FastAPI Python server.", version="0.0.1")

app.include_router(
    app_private,
    # prefix="/private",
    dependencies=[Depends(check_token)],
)
app.include_router(
    app_public,
    # prefix="/public",
)

generate_database()
