from fastapi import FastAPI
import redis
import json
import threading

app = FastAPI()
redis_client = redis.StrictRedis(host='localhost', port=6379, db=0)
pubsub = redis_client.pubsub()

# 模拟一个简单的本地数据库
local_database = {}

def handle_notification(message):
    data = json.loads(message['data'])
    action = data['action']
    key = data['key']
    if action == 'create' or action == 'update':
        value = data['value']
        local_database[key] = value
        print(f"Local database {action}d: {key} -> {value}")
    elif action == 'delete':
        if key in local_database:
            del local_database[key]
            print(f"Local database deleted: {key}")

def subscribe_notifications():
    pubsub.subscribe(**{'data_changes': handle_notification})
    pubsub.run_in_thread(sleep_time=1)

# 启动订阅线程
threading.Thread(target=subscribe_notifications).start()

@app.get("/read")
async def read_data(key: str):
    return {"key": key, "value": local_database.get(key)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
