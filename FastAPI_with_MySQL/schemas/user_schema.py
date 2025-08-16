from pydantic import BaseModel, Field
from typing import Annotated
from FastAPI_with_MySQL.models import models


class UserBase(BaseModel):
    username: str 