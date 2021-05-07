"""
Execution time header middleware
"""

from datetime import datetime
from typing import Callable, Awaitable
from fastapi.requests import Request
from fastapi.responses import Response
from starlette.middleware.base import BaseHTTPMiddleware


class ExecutionTimeMiddleware(BaseHTTPMiddleware):
    """
    Adds an execution-time header to the response
    """

    async def dispatch(self, request: Request, call_next: Callable[[Request], Awaitable[Response]]) -> Response:
        """Add execution time header"""
        start_time = datetime.utcnow()

        response = await call_next(request)

        execution_time = (datetime.utcnow() - start_time).microseconds
        response.headers["x-execution-time"] = str(execution_time)

        return response
