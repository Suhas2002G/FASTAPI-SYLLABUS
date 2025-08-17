from sqlalchemy import Integer, String, Boolean, Column
from database.db import Base


class User(Base):
    __tablename__ = "users" 
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), nullable=False, unique=True)

    def __str__(self):
        return f"{self.id}:{self.username}"


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), nullable=False)
    content = Column(String(150), nullable=False)
    user_id = Column(Integer)

    def __str__(self):
        return f"{self.title}"
 
