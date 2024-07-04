from abc import ABC, abstractmethod

"""
1. Usage Scenario
    1. 扩展一个类的功能，或给一个类添加附加职责
    2. 动态地为对象增加功能，这些功能可以被撤销
    3. 需要通过组合的方式生成功能复杂的对象
2. steps
    1. 定义组件接口，可以被装饰器和具体组件实现
    2. 具体组件：需要被装饰的原始对象
    3. 装饰器抽象类：实现组件接口，包含一个指向组件对象的引用。
        1. 装饰器的主要职责是将客户端的请求转发给组件对象。
    4. 具体装饰器：继承装饰器抽象类，实现额外的功能。
        1. 每个装饰器只负责添加一个特定的功能，符合单一职责原则。 

"""
# interface of component
class Beverage(ABC):
    @abstractmethod
    def cost(self):
        raise NotImplementedError

# concrete component
class Coffee(Beverage):
    def cost(self):
        return 5.0

# decoration abstract class
class AddonDecorator(Beverage):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage

    @abstractmethod
    def cost(self):
        raise NotImplementedError

# decoration concrete class
class Milk(AddonDecorator):
    def cost(self):
        return self._beverage.cost() + 1.5

class Sugar(AddonDecorator):
    def cost(self):
        return self._beverage.cost() + 0.5

class Chocolate(AddonDecorator):
    def cost(self):
        return self._beverage.cost() + 2.0


if __name__ == '__main__':
    beverage = Coffee()
    print(f"Cost of plain coffee: {beverage.cost()}")
    beverage_with_milk = Milk(beverage)
    print(f"Cost of plain coffee: {beverage_with_milk.cost()}")




