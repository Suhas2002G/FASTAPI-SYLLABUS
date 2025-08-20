from fastapi import FastAPI, Depends, Path, HTTPException, status
from typing import Optional
from pydantic import BaseModel, Field
from schemas import BookCreate
from database import engine, SessionLocal 
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from deps import get_db
import models
from uuid import UUID
from response import success_response, error_response


app = FastAPI()

# Create all tables in the database
models.Base.metadata.create_all(bind=engine)


# Get all books
@app.get("/book")
def get_all_books(db: Session = Depends(get_db)):
    data = db.query(models.Books).all()
    return success_response(message='Book data is fetched', data=data)



# Get single book by ID
@app.get("/book/{bid}")
def get_book_by_id(
    bid: int = Path(..., description="Book ID passed directly in the path"),
    db: Session = Depends(get_db)
):
    try:
        book = db.query(models.Books).filter(models.Books.id == bid).first()
        if book:
            return success_response(message=f'Book of ID {bid} is filtered', code=200, data=book) 
        return error_response(message=f"Book with ID {bid} not found")
    except Exception as e:
        return error_response(message='Internal Server Error', code=status.HTTP_500_INTERNAL_SERVER_ERROR, error=str(e))



# POST - Create book
@app.post("/create_books")
def create_books(book: BookCreate, db: Session = Depends(get_db)):
    book_model = models.Books()

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
        book_model = db.query(models.Books).filter(models.Books.id==book_id).first()
            
        if not book_model :
            return error_response(message=f'Book with ID {book_id} not found in DB')

        book_model.title = book.title 
        book_model.author = book.author
        book_model.description = book.description
        book_model.rating = book.rating

        db.commit()
        db.refresh(book_model)  # get latest data from DB

        return success_response(message='Book updated successfully', data=book_model)
    except Exception as e:
        db.rollback()
        return error_response(message=f'Internal server error', 
                       code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# DELETE - Delete book
@app.delete("/{book_id}")
def delete_books(book_id: int, db: Session = Depends(get_db)):
    try:
        book_model = db.query(models.Books).filter(models.Books.id == book_id).first()

        if not book_model:
            return error_response(message=f'Book with ID {book_id} not found in DB')
        
        db.delete(book_model)
        db.commit()
        return success_response(message='Book deleted successfully')
    # except SQLAlchemyException as e:

    except Exception as e:
        db.rollback()
        return error_response(message=f'Internal server error', 
                       code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                       errors=str(e)
        )

