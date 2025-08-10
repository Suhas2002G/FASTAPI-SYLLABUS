# response.py
from typing import Any, Optional
from fastapi import status


def success_response(
    data: Any,
    message: str = "Request processed successfully",
    code: int = status.HTTP_200_OK,
) -> dict:
    """
    Standard success response format.
    """
    return {
        "status": "success",
        "code": code,
        "message": message,
        "data": data
    }


def error_response(
    message: str,
    code: int = status.HTTP_400_BAD_REQUEST,
    errors: Optional[Any] = None,
) -> dict:
    """
    Standard error response format.
    """
    return {
        "status": "error",
        "code": code,
        "message": message,
        "errors": errors
    }
