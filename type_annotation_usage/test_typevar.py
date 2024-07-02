# TypeVar 用于定义一个类型变量， 可以在函数、方法或类中使用，使其能够处理多种类型。

from typing import TypeVar

# 创建类型变量Serialization,可以在注解中使用，表示任意类型
SerializationType = TypeVar("SerializationType")

# 在函数中使用类型变量
def serialize(data: SerializationType) -> SerializationType:
    # process logic
    return data

# 在类中使用类型变量
from typing import Generic
class Serializer(Generic[SerializationType]):
    # Serializer使用了泛型SerializationType,使得它可以实例化为处理做生意类型数据的序列化器。
    def __init__(self, data: SerializationType) -> None:
        self.data = data
        
    def serialize(self) -> SerializationType:
        # process logic
        return self.data