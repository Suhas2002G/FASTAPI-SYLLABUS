from fastapi import FastAPI, Depends 
from schemas.user_schema import UserBase
from schemas.post_schema import PostBase
from utils.response import success_response, error_response
from models import model
from database.db import engine
from dependencies.deps import db_dependency
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
model.Base.metadata.create_all(bind=engine)



@app.post('/users')
async def create_user(user: UserBase, db: db_dependency):
    db_user = model.User()