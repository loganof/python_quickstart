import time
from functools import wraps


def timethis(func):
    # @wraps(func)注解很重要，能够保留drbc函数的元数据
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


@timethis
def countdown(n):
    """
    Counts down
    """
    print(f"input: {n}")
    while n > 0:
        n -= 1

if __name__ == '__main__':
    # countdown(10000000)
    # print(countdown.__name__)
    # print(countdown.__doc__)
    # print(countdown.__annotations__)
    # countdown.__wrapped__(1000)
    # origin = countdown.__wrapped__
    # origin(100)
    timethis(countdown(100))