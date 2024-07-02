from abc import ABC, abstractmethod


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProductA(Product):
    def operation(self) -> str:
        return "Result of ConceretProductA"


class ConcreteProductB(Product):
    def operation(self) -> str:
        return "Result of ConceretProductB"


# Creator
class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        return f"Creator: The same creator's code has just worked with {product.operation()}"


class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteCreatorA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteCreatorB()

def client_code(creator: Creator) -> None:
    print(f"Client: {creator.some_operation()}")

client_code(ConcreteCreatorA())
client_code(ConcreteCreatorB())



