from fastapi import FastAPI
from pydantic import BaseModel
from openai import OpenAI
import os

# Tworzymy klienta OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()

class PromptRequest(BaseModel):
    prompt: str

@app.post("/api/chat")
async def chat(req: PromptRequest):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": req.prompt}],
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        return {"error": str(e)}
