from fastapi import FastAPI
import os
from dotenv import load_dotenv

load_dotenv()

print("DEBUG KEY:", os.getenv("GEMINI_API_KEY"))

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "message": "Backend is working",
        "api_key_loaded": os.getenv("GEMINI_API_KEY") is not None
    }