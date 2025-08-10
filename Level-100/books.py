from fastapi import FastAPI, Depends, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel, Field
from models import Books
from schemas import BookCreate
from database import engine, SessionLocal 
from sqlalchemy.orm import Session
from deps import get_db
import models
from uuid import UUID


app = FastAPI()

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)


# Get all books
@app.get("/book")
def get_all_books(db: Session = Depends(get_db)):
    return db.query(models.Books).all()


# Get single book by ID
@app.get("/book/{bid}")
def get_book_by_id(
    bid: int = Path(..., description="Book ID passed directly in the path"),
    db: Session = Depends(get_db)
):
    try:
        book = db.query(Books).filter(Books.id == bid).first()
        print(book)
        if book:
            return book 
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Book with ID {bid} not found"
        )
    except Exception as e:
        raise HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail=f"{e}"
    )


# POST - Create book
@app.post("/create_books")
def create_books(book: BookCreate, db: Session = Depends(get_db)):
    book_model = Books()
    book_model.title = book.title 
    book_model.author = book.author
    book_model.description = book.description
    book_model.rating = book.rating

    db.add(book_model)
    db.commit()

    return book


# # PUT - Update book
@app.put("/{book_id}")
def update_books(
    book_id: int, 
    book: BookCreate,
    db: Session = Depends(get_db)
):
    try:
        book = db.query(Books).filter(Books.id==book_id).first()
        book
    except Exception as e:
        raise HTTPException(
            detail='Internal server error',
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# # DELETE - Delete book
# @app.delete("/{book_id}")
# def delete_books(book_id: UUID):
#     for idx, existing_book in enumerate(BOOKS):
#         if existing_book.id == book_id:
#             del BOOKS[idx]
#             return {"message": f"ID {book_id} : book deleted"}
#     raise HTTPException(
#         status_code=status.HTTP_404_NOT_FOUND,
#         detail=f"ID {book_id}: book not found"
#     )
