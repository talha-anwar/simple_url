import os
from jose import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

SECRET_KEY = os.getenv("SECRET_KEY")
pwd_context = CryptContext(schemes=["bcrypt"])

def create_access_token(username: str):
    payload = {"sub": username, "exp": datetime.utcnow() + timedelta(minutes=30)}
    return jwt.encode(payload, SECRET_KEY, algorithm="HS256")

def decode_access_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=["HS256"])