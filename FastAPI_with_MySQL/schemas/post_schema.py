from pydantic import BaseModel, Field
from typing import Annotated
from FastAPI_with_MySQL.models import models


class PostBase(BaseModel):
    title: str 
    content: str 
    user_id: int 