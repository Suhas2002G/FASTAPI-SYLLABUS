from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 1. Database URL 
DATABASE_URL = "sqlite:///books.db"

# 2. Create engine using db url
engine = create_engine(DATABASE_URL, echo=True, connect_args={"check_same_thread":False})

# 3. Create Session classes that manage database operations.
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# 4. Create a base class for your ORM models. 
#    Keeps track of all models that inherit from it, so SQLAlchemy can automatically generate tables later
Base = declarative_base()

