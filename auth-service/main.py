from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

REQUEST_COUNT = Counter(
    "auth_service_requests_total",
    "Total requests to Auth Service"
)

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {"service": "Auth Service", "status": "running"}

@app.post("/login")
def login():
    REQUEST_COUNT.inc()
    return {
        "message": "Login successful",
        "token": "demo-token",
        "role": "user"
    }

@app.get("/authorize")
def authorize():
    REQUEST_COUNT.inc()
    return {
        "authorized": True,
        "role": "user"
    }

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
