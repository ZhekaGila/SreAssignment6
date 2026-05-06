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

REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP requests",
    ["service"]
)

users = [
    {"id": 1, "name": "Alice", "role": "customer"},
    {"id": 2, "name": "Bob", "role": "admin"}
]

@app.get("/")
def home():
    REQUESTS.labels(service="user").inc()
    return {"service": "User Service", "status": "running"}

@app.get("/users")
def get_users():
    REQUESTS.labels(service="user").inc()
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    REQUESTS.labels(service="user").inc()
    for user in users:
        if user["id"] == user_id:
            return user
    return {"error": "User not found"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)


