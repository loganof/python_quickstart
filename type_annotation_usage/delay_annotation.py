from __future__ import annotations
# 通过延迟解析类型，简化前向引用。在python3.11中默认启用
class Employee:
    def __init__(self, name: str, manager: Manager = None) -> None:
        self.name = name
        self.manager = manager
        
class Manager:
    def __init__(self, name: str) -> None:
        self.name = name
        self.team = []
        
        
manager1 = Manager("Bob")
employee1 = Employee("Alice", manager1)
        