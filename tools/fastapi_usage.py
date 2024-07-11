
from fastapi import FastAPI
from starlette

app = FastAPI()

@app.get("/status")
async def status():
    return "up"

# streaming
@app.get("/events")
async def events():
    return EventSourceResponse()