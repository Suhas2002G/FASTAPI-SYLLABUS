from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from schemas.user_schema import UserBase
from schemas.post_schema import PostBase
from utils.response import success_response, error_response
from models import models
from database.db import engine
from dependencies.deps import db_dependency
from core.config import get_settings

settings = get_settings()

app = FastAPI(
    debug=settings.DEBUG,
)

# Create tables (for dev only, prefer Alembic migrations in prod)
models.Base.metadata.create_all(bind=engine)



@app.post('/users')
async def create_user(user: UserBase, db: db_dependency):
    try:
        db_user = models.User(**user.model_dump())
        print(f"db_user----> {db_user}")

        db.add(db_user)
        db.commit()
        db.refresh(db_user)

        return success_response(
            message='User created successfully',
            data=db_user
        )
    except Exception as e:
        return error_response(
            message='Failed to add user',
            errors=str(e)
        )


@app.get('/user/{user_id}')
async def get_user(user_id: int, db: db_dependency):
    try:
        user = db.query(models.User).filter(models.User.id==user_id).first()
        print(user)

        if not user:
            return error_response(message='user not found', code=status.HTTP_404_NOT_FOUND)
        return success_response(message='User fetched', data=user)
    except Exception as e:
        return error_response(message='internal server error', errors=str(e))



# Add Post
@app.post('/posts')
async def add_post(post: PostBase, db: db_dependency)->dict:
    try:
        db_post = models.Post(**post.model_dump())
        print("--> ",db_post)
        db.add(db_post)
        db.commit()
        return success_response(message='Post created', code=201, data=post)
    except Exception as e:
         return error_response(message='failed to post', errors=str(e))



