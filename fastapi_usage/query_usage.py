from fastapi import FastAPI, Query
from typing import Optional

app = FastAPI()


@app.get("/items/")
async def read_items(q: Optional[str] = Query(default=None, max_length=50)):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results