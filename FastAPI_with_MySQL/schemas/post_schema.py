from pydantic import BaseModel, Field
from typing import Annotated
from models import models


class PostBase(BaseModel):
    title: str 
    content: str 
    user_id: int 

    class Config:
        orm_mode = True   # This is IMPORTANT!