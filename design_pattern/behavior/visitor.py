"""
definition:
    允许用户在不修改已有类的前提下向这些类添加新的功能。访问者模式通过将新的行为封装到一个对象中来实现这个功能，这个对象称为访问者。
structure: 
    1. Visitor(访问者接口)：定义一个访问接口，为每一个具体元素类对应一个访问方法。
    2. ConcreteVisitor(具体访问者): 实现访问者接口。
    3. Element(元素接口):定义一个accept方法，该方法接收一个访问者对象。
    4. ConcreteElement(具体元素): 实现元素接口。
    5. ObjectStructure(对象结构): 能够枚举它的元素，可以提供一个高层的接口来允许访问者访问者访问它的元素。
"""

from abc import ABC, abstractmethod
from typing import List

# 访问者接口
class Visitor(ABC):
    @abstractmethod
    def visit_concrete_element_a(self, element):
        pass

    @abstractmethod
    def visit_concrete_element_b(self, element):
        pass
    
# 具体访问者
class ConcreteVisitor1(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{element} visited by ConcreteVisitor1")
        
    def visit_concrete_element_b(self, element):
        print(f"{element} visited by ConcreteVisitor1")
class ConcreteVisitor2(Visitor):
    def visit_concrete_element_a(self, element):
        print(f"{element} visited by ConcreteVisitor2")
        
    def visit_concrete_element_b(self, element):
        print(f"{element} visited by ConcreteVisitor2")
        
        
# 元素接口
class Element(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass
    
    
# 具体元素
class ConcreteElemenA(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_element_a(self)
        
    def __str__(self) -> str:
        return "ConcreteElementA"

class ConcreteElemenB(Element):
    def accept(self, visitor: Visitor):
        visitor.visit_concrete_element_a(self)
        
    def __str__(self) -> str:
        return "ConcreteElementB"
    
# 对象结构
class ObjectStructure:
    def __init__(self) -> None:
        self._elements: List[Element]= []
        
    def add_element(self, element: Element):
        self._elements.append(element)
        
    def accept(self, visitor: Visitor):
        for element in self._elements:
            element.accept(visitor)
            
# usage

object_struture = ObjectStructure()
object_struture.add_element(ConcreteElemenA())
object_struture.add_element(ConcreteElemenB())

visitor1 = ConcreteVisitor1()
visitor2 = ConcreteVisitor2()

print("Visitor visiting elements:")
object_struture.accept(visitor1)

print("\nVisitor2 visiting elements:")
object_struture.accept(visitor2)
