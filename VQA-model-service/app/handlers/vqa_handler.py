from transformers import ViltProcessor, ViltForQuestionAnswering
from PIL import Image

# Load model and processor
processor = ViltProcessor.from_pretrained("dandelin/vilt-b32-finetuned-vqa")
model = ViltForQuestionAnswering.from_pretrained("dandelin/vilt-b32-finetuned-vqa")

def process_vqa(image: Image.Image, question: str) -> str:
    inputs = processor(image, question, return_tensors="pt")
    outputs = model(**inputs)
    logits = outputs.logits
    idx = logits.argmax(-1).item()
    answer = model.config.id2label[idx]
    return answer