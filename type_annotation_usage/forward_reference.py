
# 在类型上加上引号，这叫做前向引用。
# 前向引用：
# 1. 用于解决类型未定义：引用位置之后才定义的类型。
# 2. 避免循环引用。

class Employee:
    def __init__(self, name: str, manager: "Manager" = None) -> None:
        self.name = name
        self.manager = manager
        
class Manager:
    def __init__(self, name: str) -> None:
        self.name = name
        self.team = []
        
        
manager1 = Manager("Bob")
employee1 = Employee("Alice", manager1)
        