from fastapi import FastAPI
from app.api import router




app = FastAPI(
    title="Flow Manager Service",
    description="A generic flow manager to execute tasks sequentially with conditions",
    version="1.0.0"
)

app.include_router(router)

@app.get("/")
def flow_status():
    """
    Endpoint to verify that the Flow Manager service is running.
    """
    return {"status": "ready"}
