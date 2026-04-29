import os
import psycopg2
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
    "order_service_requests_total",
    "Total requests to Order Service"
)

def get_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

@app.get("/")
def home():
    REQUEST_COUNT.inc()
    return {"service": "Order Service", "status": "running"}

@app.get("/health")
def health():
    REQUEST_COUNT.inc()
    conn = get_connection()
    conn.close()
    return {"status": "ok", "database": "connected"}

@app.post("/orders")
def create_order():
    REQUEST_COUNT.inc()

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS orders (
            id SERIAL PRIMARY KEY,
            product_name TEXT NOT NULL,
            quantity INT NOT NULL
        );
    """)

    cursor.execute(
        "INSERT INTO orders (product_name, quantity) VALUES (%s, %s)",
        ("Laptop", 1)
    )

    conn.commit()
    cursor.close()
    conn.close()

    return {"message": "Order created successfully"}

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
