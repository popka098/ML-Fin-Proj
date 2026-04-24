from fastapi_users import BaseUserManager
from app.auth.models import User

SECRET = "SUPER_SECRET"

class UserManager(BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET