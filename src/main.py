from fastapi import FastAPI
from pydantic import BaseModel
from .swot import generate_swot_chat

app = FastAPI(title="Interactive SWOT Analyzer API")

class SWOTRequest(BaseModel):
    description: str

@app.post("/swot")
def swot_endpoint(req: SWOTRequest):
    swot_result = generate_swot_chat(req.description)
    return {"description": req.description, "swot": swot_result}

@app.get("/")
def root():
    return {"message": "SWOT Analyzer API is running"}
