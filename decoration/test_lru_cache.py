# 基于最近最少使用（least recently used, LRU)策略的缓存机制。

from functools import lru_cache

@lru_cache(maxsize=128)
def expensive_function(x):
    # 假设这是一个计算代价很高的函数
    print(f"Computing {x}")
    return x * x

print(expensive_function(4)) # 计算并缓存结果
print(expensive_function(4)) # 直接返回缓存结果，不再计算