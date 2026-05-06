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

products = [
    {"id": 1, "name": "Laptop", "price": 500},
    {"id": 2, "name": "Phone", "price": 300},
    {"id": 3, "name": "Headphones", "price": 50}
]

@app.get("/")
def home():
    REQUESTS.labels(service="product").inc()
    return {"service": "Product Service", "status": "running"}

@app.get("/products")
def get_products():
    REQUESTS.labels(service="product").inc()
    return products

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)

