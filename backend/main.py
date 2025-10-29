# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import analyze_sentiment

class TextRequest(BaseModel):
    text: str

app = FastAPI()

# --- CORS setup ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict_sentiment(request: TextRequest):
    result = analyze_sentiment(request.text)
    return result

@app.get("/")
async def root():
    return {"message": "Sentiment Analysis API is running!"}
