from fastapi import FastAPI

app = FastAPI()


# 路径参数
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    # note: 返回值item_id为int,不是str,fastapi会通过类型声明自动解析请求中的数据。
    return {"item_id": item_id}
