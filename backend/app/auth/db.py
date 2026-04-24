from fastapi import Depends
from sqlalchemy.orm import Session

from db.session import SessionLocal
from fastapi_users.db import SQLAlchemyUserDatabase
from auth.models import User
from api.deps import get_db

def get_user_db(session: Session = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)