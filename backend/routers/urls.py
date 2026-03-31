from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from dependencies import get_db
from typing import Optional
from datetime import datetime
from fastapi.responses import RedirectResponse
from utils.namegen import generate_name
from crud.url_crud import create_url, get_url, delete_url


router = APIRouter()

class ShortenRequest(BaseModel):
    original_url: str
    expiry_days: Optional[int] = None

@router.post("/shorten")
def shorten_url(request: ShortenRequest, db: Session = Depends(get_db)):
    print("expiry_days recieved:", request.expiry_days)
    short = generate_name(db)
    create_url(db, short, request.original_url, request.expiry_days)
    return {
        "short_code": short,
        "original_url": request.original_url,
        "expiry_days": request.expiry_days
    }

@router.get("/{short_url}")
def redirect(short_url: str, db: Session = Depends(get_db)):
    db_url: Optional[object] = get_url(db, short_url)
    if not db_url:
        raise HTTPException(status_code=404, detail="Not found")
    if db_url.expires_at < datetime.now().replace(tzinfo=None):
        raise HTTPException(status_code=410, detail="Link expired")
    return RedirectResponse(url=db_url.original_url)


class ShuffleRequest(BaseModel):
    original_url: str
    old_short_code: str
    expiry_days: Optional[int] = None

@router.post("/shuffle")
def shuffle_url(request: ShuffleRequest, db: Session = Depends(get_db)):
    print("shuffle request:", request)
    delete_url(db, request.old_short_code)
    short = generate_name(db)
    create_url(db, short, request.original_url, request.expiry_days)
    return {
        "short_code": short,
        "original_url": request.original_url,
        "expiry_days": request.expiry_days
    }