import requests
import time

data = "你好世界！" * 500

input_data = [
    [data] * 8,
    [data] * 12,
    [data] * 32,
    # [data] * 64,
    # [data] * 128,
    # [data] * 256,
    # [data] * 512,
    # [data] * 1024,
]
# BS = [1, 16, 32, 64, 128, 256, 512, 1024]
BS = [8, 12, 32]
TIME_COST = []


"""
并发调用
"""
import concurrent.futures
from concurrent.futures import wait
from concurrent.futures import ThreadPoolExecutor, as_completed

threadpool = ThreadPoolExecutor(max_workers=1024)


def one_call(inputs):
    r = requests.get("http://127.0.0.1:8000/random")
    if r.status_code == 200:
        return r.json()
    else:
        print(f"error: {r.status_code}: {r.text}, len:{len(inputs)}")
        return []


while True:
    TIME_COST = []
    for bs, dt in zip(BS, input_data):
        # 进行推理
        start_time = time.time()
        assert len(dt) == bs
        tasks = []
        for one_input in dt:  # 并发完成bs个推理
            tasks.append(threadpool.submit(one_call, one_input))
        res = []
        for future in as_completed(tasks):
            _ = future.result()  # 等bs个推理完成后再统计时长
            assert len(_) == len([[]])
            res.extend(_)
            # print(_)
        end_time = time.time()
        cost = end_time - start_time
        TIME_COST.append(cost)
        # print(f'len: {len(res)}')

    for i, tc in enumerate(TIME_COST):
        print(f"bs: {BS[i]}, total cost: {tc}")
