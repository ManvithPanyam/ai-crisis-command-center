import os
import time
import json
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "gemini-2.5-flash"

GEMINI_URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"{GEMINI_MODEL}:generateContent?key={GEMINI_API_KEY}"
)

class AnalyzeRequest(BaseModel):
    text: str

class AnalyzeResponse(BaseModel):
    summary: str
    severity: str
    key_points: list[str]
    recommended_actions: list[str]

@app.post("/analyze", response_model=AnalyzeResponse)
async def analyze(data: AnalyzeRequest):

    if not GEMINI_API_KEY:
        raise HTTPException(status_code=500, detail="API key missing")

    prompt = f"""
You are an AI crisis analysis engine.

Return ONLY valid JSON:
{{
  "summary": "string",
  "severity": "Low or Medium or High",
  "key_points": ["string"],
  "recommended_actions": ["string"]
}}

Crisis:
{data.text}
"""

    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": prompt}]
            }
        ],
        "generationConfig": {
            "response_mime_type": "application/json"
        }
    }

    max_retries = 3

    for attempt in range(max_retries):
        response = requests.post(
            GEMINI_URL,
            json=payload,
            headers={"Content-Type": "application/json"}
        )

        if response.status_code == 200:
            break

        if response.status_code == 503:
            time.sleep(2)  # wait and retry
        else:
            break

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail=response.text)

    raw = response.json()

    try:
        text_output = raw["candidates"][0]["content"]["parts"][0]["text"]
        parsed = json.loads(text_output)
    except Exception:
        raise HTTPException(status_code=500, detail=raw)

    return parsed