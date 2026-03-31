import os
from jose import jwt
from datetime import datetime, timedelta

SECRET_KEY = os.getenv("SECRET_KEY")

def create_access_token(username: str):
    payload = {"sub": username, "exp": datetime.utcnow() + timedelta(minutes=30)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")