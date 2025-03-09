from typing import Union
from app.api.vqa import router as vqa_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

app = FastAPI()

origins = [
    "http://localhost:9000",
    "http://127.0.0.1:9000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.include_router(vqa_router, prefix="/vqa", tags=["Visual Question Answering"])

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

@app.get("/health")
def health():
    return {"Hello": "Welcome to the VQA API!"}
