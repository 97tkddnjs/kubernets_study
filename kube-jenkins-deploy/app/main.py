from fastapi import FastAPI
from datetime import datetime
import os
import socket

app = FastAPI(
    title="FastAPI K8s Demo",
    description="Jenkins CI/CD with Kubernetes",
    version=os.getenv("APP_VERSION", "1.0.0")
)

@app.get("/")
async def root():
    return {
        "message": "Welcome to FastAPI on Kubernetes!",
        "version": os.getenv("APP_VERSION", "unknown"),
        "build": os.getenv("BUILD_NUMBER", "unknown"),
        "hostname": socket.gethostname(),
        "timestamp": datetime.now().isoformat()
    }

@app.get("/health")
async def health():
    return {
        "status": "healthy",
        "version": os.getenv("APP_VERSION", "unknown"),
        "timestamp": datetime.now().isoformat()
    }

@app.get("/api/info")
async def info():
    return {
        "app": "fastapi-k8s-demo",
        "version": os.getenv("APP_VERSION", "unknown"),
        "build": os.getenv("BUILD_NUMBER", "unknown"),
        "hostname": socket.gethostname(),
        "ip": socket.gethostbyname(socket.gethostname()),
        "environment": os.getenv("ENVIRONMENT", "development")
    }

@app.get("/api/test")
async def test():
    """테스트 엔드포인트"""
    return {
        "status": "success",
        "message": "API is working correctly!",
        "data": {
            "test1": "passed",
            "test2": "passed",
            "test3": "passed"
        }
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)