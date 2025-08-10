from database import SessionLocal
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# get_db() solves this by:
# Creating a new session for each request.
# Yielding it to the route handler so you can use it.
# Closing it automatically after the request is done (even if an error happens).