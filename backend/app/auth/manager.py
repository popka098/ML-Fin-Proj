from fastapi_users import BaseUserManager
from app.auth.models import User

from dotenv import load_dotenv
import os

load_dotenv()
SECRET = os.getenv("SUPER_SECRET")

class UserManager(BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET