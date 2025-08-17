from pydantic import BaseModel, Field
from typing import Annotated
from models import models


class UserBase(BaseModel):
    username: str 