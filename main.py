from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

# Wczytaj klucz API z zmiennej środowiskowej
openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/api/chat")
async def chat(req: PromptRequest):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": req.prompt}],
        )
        return {"response": response.choices[0].message["content"]}
    except Exception as e:
        return {"error": str(e)}
