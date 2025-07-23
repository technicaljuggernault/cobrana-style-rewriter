from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()

class RewriteRequest(BaseModel):
    reference_text: str
    target_text: str

class RewriteResponse(BaseModel):
    styled_text: str

@app.post("/rewrite-to-match-style", response_model=RewriteResponse)
def rewrite_text(data: RewriteRequest):
    styled = f"In the style of: '{data.reference_text}' — here's your text: '{data.target_text}'"
    return {"styled_text": styled}

# ----------------- New Action Below -----------------

class ToneCheckRequest(BaseModel):
    text: str

class ToneCheckResponse(BaseModel):
    ai_like_score: float
    recommend_rewrite: bool

@app.post("/detect-ai-generated-tone", response_model=ToneCheckResponse)
def detect_ai_generated_tone(data: ToneCheckRequest):
    # Example scoring logic (replace with AI model or OpenAI call if you want)
    overused_phrases = ["in today’s ever-evolving", "leverage synergies", "unlock new opportunities", "digital transformation"]
    score = 0.0
    for phrase in overused_phrases:
        if phrase in data.text.lower():
            score += 0.25

    score = min(1.0, round(score + random.uniform(0, 0.2), 2))
    return {
        "ai_like_score": score,
        "recommend_rewrite": score > 0.7
    }
