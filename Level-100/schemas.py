from pydantic import BaseModel, Field

# Pydantic model class
class BookCreate(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1, max_length=100)
    description: str = Field(min_length=1, max_length=1000)
    rating: int = Field(gt=-1, lt=6)  # 0-5

