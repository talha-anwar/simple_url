from sqlalchemy.orm import Session
from models.url import URL
from datetime import datetime, timedelta

def create_url(db: Session, short_url: str, original_url: str, expiry_days: int = None):
    if expiry_days:
        expires_at = datetime.now() + timedelta(days=expiry_days)
    else:
        expires_at = datetime.now() + timedelta(hours=24)
    
    print("expires_at being set:", expires_at)

    db_url = URL(short_url=short_url, original_url=original_url, expires_at=expires_at)
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url

def get_url(db: Session, short_url: str):
    return db.query(URL).filter(URL.short_url == short_url).first()

def delete_url(db: Session, short_url: str):
    db_url = db.query(URL).filter(URL.short_url == short_url).first()
    if db_url:
        db.delete(db_url)
        db.commit()