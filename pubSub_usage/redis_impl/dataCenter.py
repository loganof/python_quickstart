from fastapi import FastAPI
import redis
import json

app = FastAPI()
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)

# 模拟一个简单的数据库
database = {}

@app.post("/create")
async def create_data(key: str, value: str):
    database[key] = value
    redis_client.publish('data_changes', json.dumps({'action': 'create', 'key': key, 'value': value}))
    return {"status": "created", "key": key, "value": value}

@app.put("/update")
async def update_data(key: str, value: str):
    if key in database:
        database[key] = value
        redis_client.publish('data_changes', json.dumps({'action': 'update', 'key': key, 'value': value}))
        return {"status": "updated", "key": key, "value": value}
    return {"status": "key not found", "key": key}

@app.delete("/delete")
async def delete_data(key: str):
    if key in database:
        del database[key]
        redis_client.publish('data_changes', json.dumps({'action': 'delete', 'key': key}))
        return {"status": "deleted", "key": key}
    return {"status": "key not found", "key": key}

@app.get("/read")
async def read_data(key: str):
    return {"key": key, "value": database.get(key)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
