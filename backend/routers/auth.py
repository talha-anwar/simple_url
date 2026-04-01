from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from models.user import User
from dependencies import get_db
from utils.jwt import pwd_context
from utils.jwt import create_access_token
from fastapi.responses import RedirectResponse
from crud.user_crud import create_user, get_user_by_username, delete_user_by_username
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter()

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

@router.post("/auth/register")
def register_user(request: RegisterRequest, db: Session = Depends(get_db)):
    if not get_user_by_username(db, request.username):
        print("new user registered:", request.username)
        create_user(db, request.username, request.email, request.password)
        return {
            "username": request.username,
            "email": request.email,
        }
    else:
        raise HTTPException(status_code=409, detail="Username already exists")
    
# class LoginRequest(BaseModel):
#     username: str
#     password: str

@router.post("/auth/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = get_user_by_username(db, form_data.username)
    if user:
        stored_pass = user.hashed_password
        if pwd_context.verify(form_data.password, stored_pass):
            return {
                "access_token": create_access_token(form_data.username),
                "token_type": "bearer"
            }
        else:
            raise HTTPException(status_code=401, detail="BOMBOKLATT!!")
    else:
        raise HTTPException(status_code=401, detail="BOMBOKLATT!!")
