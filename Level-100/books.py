from typing import Optional
from fastapi import FastAPI, Path, HTTPException, status
from pydantic import BaseModel, Field
from uuid import UUID

app = FastAPI()

# Pydantic model class
class BookCreate(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=1000)
    rating: int = Field(gt=-1, lt=6)  # 0-5

# List of all books
BOOKS: list[BookCreate] = []


# Get all books
@app.get("/book")
def get_all_books():
    return BOOKS


# Get single book by ID
@app.get("/book/{bid}")
def get_book_by_id(
    bid: UUID = Path(..., description="Book ID passed directly in the path")
):
    for book in BOOKS:
        if book.id == bid:
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Book with ID {bid} not found"
    )


# POST - Create book
@app.post("/create_books")
def create_books(book: BookCreate):
    BOOKS.append(book)
    return book


# PUT - Update book
@app.put("/{book_id}")
def update_books(book_id: UUID, book: BookCreate):
    for idx, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            BOOKS[idx] = book
            return book
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"ID {book_id}: book not found"
    )


# DELETE - Delete book
@app.delete("/{book_id}")
def delete_books(book_id: UUID):
    for idx, existing_book in enumerate(BOOKS):
        if existing_book.id == book_id:
            del BOOKS[idx]
            return {"message": f"ID {book_id} : book deleted"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"ID {book_id}: book not found"
    )
