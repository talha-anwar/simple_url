from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models.db import engine
from models.url import Base
from routers.urls import router as urls_router


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)
app.include_router(urls_router)