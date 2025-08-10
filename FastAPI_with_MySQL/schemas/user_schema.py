from pydantic import BaseModel, Field
from typing import Annotated
from models import model


class UserBase(BaseModel):
    username: str 