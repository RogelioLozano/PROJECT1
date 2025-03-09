from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.handlers.vqa_handler import process_vqa
from app.utils.image_processing import decode_base64_image
import rich

router = APIRouter()

class VQARequest(BaseModel):
    image_base64: str
    question: str

class VQAResponse(BaseModel):
    answer: str

@router.post("", response_model=VQAResponse)
async def vqa_endpoint(payload: VQARequest):
    try:
        # rich.print(payload)
        image = decode_base64_image(payload.image_base64)
        answer = process_vqa(image, payload.question)
        return {"answer": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))