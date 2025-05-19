from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json
from pathlib import Path

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load demo_data.json once at startup
data_file = Path("data/demo_data.json")
with open(data_file, "r") as f:
    demo_data = json.load(f)

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    message = body.get("message", "").lower()

    # Try to match input to a known question
    response = demo_data.get(message, "I'm not sure how to respond to that yet.")

    return JSONResponse({"response": response})
