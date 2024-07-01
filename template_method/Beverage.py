from abc import ABC, abstractmethod

# template method
"""
1. abstract class
    1. 定义算法的骨架。
    2. 包含一个模板方法（定义了算法的基本步骤）。
    3. 包含一些抽象的方法，由子类实现。
2. concrete class
    1. 实现抽象类的抽象方法
3. usage case
    1. 多个子类有仅有的方法，并且逻辑基本相同，例如制作不同类型的饮料，不同类型的文件解析。

"""
class Beverage(ABC):
    def prepare_beverage(self):
        self.boil_water()
        self.brew()
        self.pour_in_cup()
        self.add_condiments()

    def boil_water(self):
        print("Boiling water")

    def pour_in_cup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self):
        raise NotImplementedError()

    @abstractmethod
    def add_condiments(self):
        raise NotImplementedError()


class Tea(Beverage):
    def brew(self):
        print("Steeping the tea")

    def add_condiments(self):
        print("Adding lemon")

class Coffe(Beverage):
    def brew(self):
        print("Dripping coffe through filter")

    def add_condiments(self):
        print("Adding sugar and milk")


# use template method to make beverage
def make_beverage(beverage: Beverage):
    beverage.prepare_beverage()

tea = Tea()
coffe = Coffe()
make_beverage(tea)
print()
make_beverage(coffe)