"""
Annotated在python3.9加入标准库，允许用户在类型提示中添加额外的信息。
作用：
1. fastapi中请求参数验证
2. 依赖注入
3. 为字段提供额外的元数据
"""

from fastapi import FastAPI, Query
from typing import Annotated, Optional
from pydantic import BaseModel, Field

app = FastAPI()


# 参数验证
@app.get("/items/")
def read_items(q: Annotated[str, Query(min_length=3, max_length=50)]):
    return {"q": q}


# 为字段提供额外的元数据
class Item(BaseModel):
    name: Annotated[str, Field(min_length=3)]
    # description: Annotated[str | None, Field(default=None, max_length=300)]
    description: Annotated[Optional[str], Field(default=None, max_length=300)]


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("annotated_usage:app", host="127.0.0.1", port=7888)
