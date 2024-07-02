# 将对象的属性或字段转换成字典格式, 不是内置方法，是一种常见的约定，需要自己实现
# 对于简单的类，可以使用内置方法__dict__属性

from typing import Text, Any, Dict

class Person:
    def __init__(self, name: Text, age: int, email: Text) -> None:
            self.name = name
            self.age = age
            self.email = email
            
    def as_dict(self)-> Dict[Text, Any]:
        return {
            'name': self.name,
            'age': self.age,
            'email': self.email
        }
        
        
person = Person(name="Alice", age=30, email="123456@example.com")
person_dict = person.as_dict()
print(person_dict)
    