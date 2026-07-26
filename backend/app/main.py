from fastapi import FastAPI
from app.routers.health import router as health_router

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to SentinelPay"
    }

app.include_router(health_router)