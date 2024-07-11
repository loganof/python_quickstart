"""
hasattr 用于在运行时检查对象是否具有给定的属性。

语法：

hasattr(object, name)

参数：

object -- 要检查属性的对象。
name -- 字符串，表示属性的名字。
返回值：

如果对象具有给定的属性，返回 True，否则返回 False。

结合getattr()和hasattr()可以简化代码，提高代码的可读性。    
"""

class MyClass:
    def __init__(self) -> None:
        self.name = 'Alice'
        
    def greet(self):
        return "Hello!"
    
obj = MyClass()

# 检查对象是否有属性 'name'
print(hasattr(obj, 'name'))

print(hasattr(obj, 'greet'))

print(hasattr(obj, 'age'))

name = getattr(obj, 'name', 'unknown') 
print(name)

age = getattr(obj, 'age', 0) 
print(age)
