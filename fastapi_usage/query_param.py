from typing import Optional
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


# 查询参数
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    # 声明的参数不是路径参数时，路径操作函数会把该参数自动解释为查询参数
    return fake_items_db[skip : skip + limit]


@app.get("items/option/{item_id}")
async def read_item(item_id: str, q: Optional[str] = None):
    # item_id是路径参数，q是查询参数
    # 查询参数q是可选的，默认值为None
    if q:
        return {"item_id": item_id, "q": q}
    return {"item_id", item_id}


@app.get("/items/required/{item_id}")
async def read_user_item(item_id: str, needy: str):
    # needy是必填的
    item = {"item_id": item_id, "needy": needy}
    return item
