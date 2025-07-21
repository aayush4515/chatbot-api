from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import openai
import os
from dotenv import load_dotenv

# load dotenv to connect api key from .env file
load_dotenv()

# retrieve the api key stored in .env under OPENAI_API_KEy
openai.api_key = os.getenv("OPENAI_API_KEY")

# create an instance of FastAPI application called app
app = FastAPI()

# request body schema
class PromptRequest(BaseModel):
    prompt: str

# API endpoint
@app.post("/ask")
async def handle_prompt(request: PromptRequest):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a tutor helping Python programmers learn C++. "},
                {"role": "user", "content": request.prompt}
            ]
        )
        answer = response.choices[0].message.content
        return {"response": answer}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
