# Mixin是一种设计模式，用于将可重用的方法添加到多个类中，而不需要使用继承的全部功能。Mixin一般不单独实例化。
# 使用mixin还是decorator?

class LoggerMixin:
    def log(self, message: str) -> None:
        print(f"[LOG] {message}")
        

class TimestampMixin:
    def current_timestamp(self) -> str:
        from datetime import datetime
        return datetime.now().isoformat()
    

class MyClass(LoggerMixin, TimestampMixin):
    def do_something(self) -> None:
        self.log("Doing something...")
        print(f"Current timestamp: {self.current_timestamp()}")
        
        
obj = MyClass()
obj.do_something()