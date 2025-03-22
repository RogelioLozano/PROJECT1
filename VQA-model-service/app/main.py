from typing import Union
from app.api.vqa import router as vqa_router

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os
from fastapi.middleware.gzip import GZipMiddleware

app = FastAPI()

load_dotenv()  # take environment variables from .env.

# if the environment variable is not set, the default value is used
prod_url = os.getenv("PRODUCTION_URL", "https://project-1-git-main-rogeliolozanos-projects.vercel.app")


origins = [
    "glorious-magic.railway.internal",
    prod_url,
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow specific origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

app.add_middleware(GZipMiddleware, minimum_size=1000)  # Enable gzip


app.include_router(vqa_router, prefix="/vqa", tags=["Visual Question Answering"])


# Code of your application, which uses environment variables (e.g. from `os.environ` or
# `os.getenv`) as if they came from the actual environment.

@app.get("/health")
@app.head("/health", status_code=204)
def health():
    return {"Hello": "Welcome to the VQA API!"}
