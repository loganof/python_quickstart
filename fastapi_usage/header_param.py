from typing import Annotated
from fastapi import FastAPI, Header


app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: int, client_id: Annotated[str | None, Header()] = None):
    print(f"client_id: {client_id}")
    return {"item_id": item_id}
