from fastapi import FastAPI
from app.api import router




app = FastAPI(
    title="Flow Manager Service",
    description="A generic flow manager to execute tasks sequentially with conditions",
    version="1.0.0"
)

app.include_router(router)

@app.get("/health")
def health_check():
    """
    Health check endpoint to verify the service is running.
    """
    return {"status": "ok Get Home Page"}
