# @dataclass 是python3.7引入的一个装饰器，主要是简化类的创建，尤其用于存储数据的类。通过@dataclass，可以自动生成一些常用的特殊方法， 如"__init__,__repr__, __eq__"等。


from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    
    
p1 = Person(name="Alice", age=30)
p2 = Person(name="Bob", age=25)
# 自动生成__repr方法
print(p1)
# 自动生成__eq__方法
print(p1 == p2)