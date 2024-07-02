import threading

lock = threading.Lock()

with lock:
    # 线程安全的代码
    pass

# 锁在这里自动释放