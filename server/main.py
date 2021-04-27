"""
Main application start point.
"""

from fastapi import FastAPI, Depends
from server.api.public import app_public
from server.api.private import app_private
from server.middleware.access_control import check_token
from server.services.database import generate_database_schema

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

generate_database_schema()

if __name__ == "__main__":
    import uvicorn

    print("Run uvicorn")
    uvicorn.run("server:app", host="0.0.0.0", workers=1, port=5000)
    print("Stop uvicorn")
