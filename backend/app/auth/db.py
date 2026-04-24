from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy.orm import Session
from app.auth.models import User

def get_user_db(session: Session):
    yield SQLAlchemyUserDatabase(session, User)