from fastapi import FastAPI
from pydantic import BaseModel

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
