from fastapi import FastAPI
from kafka import KafkaConsumer
import json
import threading

app = FastAPI()

consumer = KafkaConsumer('data_changes',
                         bootstrap_servers='localhost:9092',
                         value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                         group_id='service_b')

# 模拟一个简单的本地数据库
local_database = {}

def handle_notification(message):
    data = message.value
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
    for message in consumer:
        handle_notification(message)

# 启动订阅线程
threading.Thread(target=subscribe_notifications).start()

@app.get("/read")
async def read_data(key: str):
    return {"key": key, "value": local_database.get(key)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
