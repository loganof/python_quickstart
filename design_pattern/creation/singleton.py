import threading


class SingletonMeta(type):
    """
    a thread safe meta class
    """
    _instances = {}
    _lock = threading.Lock()
    

    def __call__(cls, *args, **kwargs):
        with cls._lock:  # 确保线程安全
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]
    
    
class Singleton(metaclass=SingletonMeta):
    def __init__(self) -> None:
        self.value = None
        
        
        
# usage
singleton1 = Singleton()

singleton1.value = "Singleton Instance 1"

singleton2 = Singleton()
print(singleton2.value)
print(singleton1 is singleton2)