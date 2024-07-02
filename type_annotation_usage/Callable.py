from typing import Callable, Any
from functools import wraps

# Callable[..., Any]是一个类型注解，表示f接受任意数量、任意类型参数的函数，并返回一个Any类型的结果

# 装饰器
def agent_must_be_ready(f: Callable[..., Any]) -> Callable[..., Any]:
    @wraps
    def wrapper(self, *args, **kwargs):
        if self.is_ready():
            return f(self, *args, **kwargs)
        else:
            raise RuntimeError("Agent not ready yet.")
    return wrapper  

