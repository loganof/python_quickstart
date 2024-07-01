from pydantic import BaseModel
# BaseModel是Pydantic库提供的一个类，用于定义数据模型。相比数据类，BaseModel提供了更多的功能：类型检查、序列化与反序列化

class Person(BaseModel):
    name : str
    age : int
    email: str

person1 = Person(name="Alice", age=30, email="1234567@qq.com")

person_dict = person1.__dict__
print(person_dict)