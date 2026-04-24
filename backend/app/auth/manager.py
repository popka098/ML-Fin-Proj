from fastapi import HTTPException
from fastapi_users import BaseUserManager
from auth.models import User
from uuid import UUID

from dotenv import load_dotenv
import os

load_dotenv()
SECRET = os.getenv("SUPER_SECRET")
class UserManager(BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    def parse_id(self, user_id: str) -> int:
        try:
            return int(user_id)
        except ValueError:
            raise HTTPException(404, "Invalid user id")