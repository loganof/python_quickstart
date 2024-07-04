"""
原型模式
definition:
    通过复制现有对象来创建新对象，而不是通过类的实例化来创建对象。这个模式适用于需要大量相似对象的场景，避免重复的初始化。
steps:
    1. 定义一个原型接口：包含一个用于克隆对象的方法。
    2. 创建具体原型类：实现原型接口，并具体实现克隆方法。
    3. 客户端使用原型对象: 当需要创建新对象时，客户端调用原型的克隆方法。
advantages:
    1. 简化对象的创建
    2. 提高性能
    3. 更加灵活：不依赖具体类的构造函数
disadvantages:
    1. 小心处理深/浅拷贝的问题
"""

import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class ConcretePrototype1(Prototype):
    def __init__(self, field1, filed2) -> None:
        self.field1 = field1
        self.field2 = filed2
        
    def __str__(self) -> str:
        return f"ConcretePrototype1(field1={self.field1}, field2={self.field2})"
    
    
# 创建一个具体的原型对象
prototype1 = ConcretePrototype1("value1", [1, 2, 3])
# 克隆对象
cloned_prototype1 = prototype1.clone()

# 修改克隆对象的属性
cloned_prototype1.field1 = "new value"
cloned_prototype1.field2.append(4)

# 打印原型对象和克隆对象
print(prototype1)
print(cloned_prototype1)