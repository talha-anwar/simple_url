from models.db import SessionLocal
from passlib.context import CryptContext
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from utils.jwt import decode_access_token
from crud.user_crud import get_user_by_username
from sqlalchemy.orm import Session
from jose.exceptions import JWTError

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

pwd_context = CryptContext(schemes=["bcrypt"])
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(db: Session = Depends(get_db), token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
        if payload:
            user = get_user_by_username(db, payload["sub"])
            if user:
                return user
            else:
                raise HTTPException(status_code=401, detail="User does not exist")
    except JWTError:
        raise HTTPException(status_code=401, detail="Expired or Invalid token")
