from fastapi import FastAPI
from app.routers.health import router as health_router
from app.routers.auth import router as auth_router

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "Welcome to SentinelPay"
    }

app.include_router(health_router)
app.include_router(auth_router)