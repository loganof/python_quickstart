"""
property: 把类的方法伪装成属性调用的方式。

"""
class Person:
    def __init__(self, name: str, age: int) -> None:
        self._name = name
        self._age = age
        
    @property
    def age(self):
        return self._age 
    
logan = Person("Logan", 18)
print(logan.age)