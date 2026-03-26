from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from models.db import SessionLocal, engine
from models.url import Base
from utils.namegen import generate_name
from crud.url_crud import create_url, get_url
from datetime import datetime, timezone
from typing import Optional
from crud.url_crud import create_url, get_url, delete_url

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

class ShortenRequest(BaseModel):
    original_url: str
    expiry_days: Optional[int] = None

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/shorten")
def shorten_url(request: ShortenRequest, db: Session = Depends(get_db)):
    print("expiry_days recieved:", request.expiry_days)
    short = generate_name(db)
    create_url(db, short, request.original_url, request.expiry_days)
    return {
        "short_code": short,
        "original_url": request.original_url,
        "expiry_days": request.expiry_days
    }

@app.get("/{short_url}")
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

@app.post("/shuffle")
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


#testing if things work