from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class Prompt(BaseModel):
    prompt: str

@app.post("/api/chat")
async def chat_endpoint(data: Prompt):
    prompt = data.prompt
    response = f"To jest odpowiedź AI na: '{prompt}'"
    return {"response": response}

@app.post("/api/image")
async def image_endpoint(data: Prompt):
    sample_images = [
        "https://via.placeholder.com/512x512.png?text=Sample+Image+1",
        "https://via.placeholder.com/512x512.png?text=Sample+Image+2",
        "https://via.placeholder.com/512x512.png?text=Sample+Image+3"
    ]
    image_url = random.choice(sample_images)
    return {"image_url": image_url}
