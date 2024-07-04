"""
definition:
    将抽象与实现部分分离，使它们可以独立变化。
steps: 
    1. 抽象部分(abstraction): 定义抽象类，并包含一个对实现部分的引用。
    2. 扩充抽象部分(Refined Abstraction): 继承抽象类，扩展抽象部分的接口。
    3. 实现部分(Implementor): 定义实现类接口， 不一定要和抽象部分完全一致。
    4. 具体实现部分(Concrete Implementor): 具体实现部分接口的。
"""

# 实现部分接口
class Implementor:
    def operation_implemention(self):
        raise NotImplementedError
    
# 具体实现部分A
class ConcreteImplementorA(Implementor):
    def operation_implemention(self):
        return "ConcreteImplementorA: Here's a result on the platform A."
    
    
# 具体实现部分B
class ConcreteImplementorB(Implementor):
    def operation_implemention(self):
        return "ConcreteImplementorB: Here's a result on the platform B."
    
# 抽象部分
class Abstraction:
    def __init__(self, implementor: Implementor) -> None:
        self.implementor = implementor
        
    def operation(self):
        return self.implementor.operation_implemention()
    
    
# 扩充抽象部分
class ExtendedAbstraction(Abstraction):
    def operation(self):
        return f"ExtendedAbstraction: Extended operation with: \n{self.implementor.operation_implemention()}"
    
    
# client
def client_code(abstraction: Abstraction):
    print(abstraction.operation())
    
    
# 使用桥接
implementor_a = ConcreteImplementorA()
abstraction = Abstraction(implementor_a)
client_code(abstraction)

implementor_b = ConcreteImplementorB()
extended_abstraction = Abstraction(implementor_b)
client_code(extended_abstraction)