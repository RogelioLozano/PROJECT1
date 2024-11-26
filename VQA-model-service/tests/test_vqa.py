from fastapi.testclient import TestClient
from app.main import app
import os

client = TestClient(app)

def test_health():
    response = client.get("/health")
    if response.status_code != 200:
        print(response.json())
    assert response.json() == {"Hello": "Welcome to the VQA API!"}

def test_vqa_endpoint():
    response = client.post(
        "/vqa/",
        json={
            "image_base64": os.getenv("IMAGE_TEST_BASE64"),
            "question": "What is in the image?"
        }
    )
    assert response.status_code == 200

