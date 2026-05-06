from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["service"]
)

messages = []

class Message(BaseModel):
    user: str
    text: str

@app.get("/")
def home():
    REQUEST_COUNT.labels(service="chat").inc()
    return {"service": "Chat Service", "status": "running"}

@app.post("/messages")
def send_message(message: Message):
    REQUEST_COUNT.labels(service="chat").inc()
    messages.append(message.dict())
    return {"message": "Message sent", "data": message}

@app.get("/messages")
def get_messages():
    REQUEST_COUNT.labels(service="chat").inc()
    return messages

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
