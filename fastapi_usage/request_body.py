from pydantic import BaseModel
from typing import Optional, Annotated
from fastapi import FastAPI, Body


class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


# 请求体(BaseModel形式)
@app.post("/items/")
async def create_item(item: Item):
    return item


@app.post("/items/single/")
async def create_item(item: Annotated[int, Body()]):
    return item


# 请求体 + 路径参数
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.__dict__}


# 请求体 + 路径参数 + 查询参数
@app.put("/items/update/{item_id}")
async def update_item(item_id: int, item: Item, q: Optional[str] = None):
    result = {"item_id": item_id, **item.__dict__}
    if q:
        result.update({"q": q})
    return result
