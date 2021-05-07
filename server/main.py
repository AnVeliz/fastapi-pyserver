"""
Main application start point.
"""

from fastapi import FastAPI, Depends
from server.api.public import app_public
from server.api.private import app_private
from server.middleware import check_token, ExecutionTimeMiddleware

app = FastAPI(title="FastAPI PyServer", description="Simple FastAPI Python server.", version="0.0.1")

app.include_router(
    app_private,
    # prefix="/private",
    dependencies=[Depends(check_token)],
)
app.include_router(
    app_public,
    dependencies=[],
    # prefix="/public",
)

app.add_middleware(ExecutionTimeMiddleware)


if __name__ == "__main__":
    import uvicorn

    print("Run uvicorn")
    uvicorn.run("server:app", host="0.0.0.0", workers=1, port=5000)
    print("Stop uvicorn")
