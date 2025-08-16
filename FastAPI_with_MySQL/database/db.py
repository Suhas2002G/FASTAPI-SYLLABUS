from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from core.config import get_settings

# importing evn variables from config 
settings = get_settings()

# 1. Database URL 
DATABASE_URL = settings.DATABASE_URL

# 2. Create engine using db url
engine = create_engine(DATABASE_URL)   # echo=True

# 3. Create Session classes that manage database operations.
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)

# 4
Base = declarative_base()
