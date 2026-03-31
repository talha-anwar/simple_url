from sqlalchemy import Column, String, Integer, TIMESTAMP, text, ForeignKey
from datetime import datetime, timezone, timedelta
from .db import Base

class URL(Base):
    __tablename__ = "urls"

    short_url = Column(String(100), primary_key=True, index=True)
    original_url = Column(String(2048), nullable=False)
    created_at = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    expires_at = Column(TIMESTAMP, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)