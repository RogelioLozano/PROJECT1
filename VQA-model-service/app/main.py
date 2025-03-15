from typing import Union
from app.api.vqa import router as vqa_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

app = FastAPI()

load_dotenv()  # take environment variables from .env.

origins = [
    "http://127.0.0.1:9000",
     os.getenv("PRODUCTION_URL"),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(vqa_router, prefix="/vqa", tags=["Visual Question Answering"])


# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

@app.get("/health")
def health():
    return {"Hello": "Welcome to the VQA API!"}
