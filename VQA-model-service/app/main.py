from typing import Union
from app.api.vqa import router as vqa_router

from fastapi import FastAPI
from dotenv import load_dotenv

app = FastAPI()

app.include_router(vqa_router, prefix="/vqa", tags=["Visual Question Answering"])

load_dotenv()  # take environment variables from .env.

# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

@app.get("/health")
def health():
    return {"Hello": "Welcome to the VQA API!"}
