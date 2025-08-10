from fastapi import FastAPI, Path, Query, Request, HTTPException, status
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

# PATH PARAMETER
@app.get('/book_by_path/{bid}')
def get_book_by_id(
    bid: str = Path(..., description="Book ID passed directly in the path")
):
    """
    Get book details using a path parameter.

    Path parameters are part of the URL path itself and are required.
    Example: /book_by_path/123

    Args:
        bid (str): The ID of the book passed via the URL path.

    Returns:
        dict: Book ID and its generated name.
    """
    return {
        "id": bid,
        "name": f"start-{bid}"
    }


# QUERY PARAMETER
@app.get('/book_by_query')
def get_book(
    bid: str = Query(..., description="Book ID passed as a query parameter")
):
    """
    Get book details using a query parameter.

    Query parameters are optional by default and passed after a `?` in the URL.
    Example: /book_by_query?bid=123

    Args:
        bid (str): The ID of the book passed via the query string.

    Returns:
        dict: Book ID and its generated name.
    """
    return {
        "id": bid,
        "name": f"start-{bid}"
    }

