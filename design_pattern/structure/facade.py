"""
definition:
    为复杂子系统提供一个统一的接口，使子系统更容易使用。外观模式通过定义一个高层接口，使得客户端可以更方便地与子系统进行交互，而无需了解子系统的复杂实现细节。
structure: 
    1. facade:提供一个简单的接口，用来访问子系统中的一组接口。
    2. subSystem: 包含实际的业务逻辑的类，它们实现子系统的功能。子系统不知道外观的存在，它们相互之间也可以直接交互。
"""

# sub system A
class SubSystemA:
    def operation_a1(self):
        return "Subsystem A, Method A1"
    def operation_a2(self):
        return "Subsystem A, Method A2"
    
class SubSystemB:
    def operation_b1(self):
        return "Subsystem A, Method B1"
    def operation_b2(self):
        return "Subsystem A, Method B2"
class SubSystemC:
    def operation_c1(self):
        return "Subsystem A, Method C1"
    def operation_c2(self):
        return "Subsystem A, Method C2"
    
    
# facade class
class Facade:
    def __init__(self) -> None:
        self.subsystem_a = SubSystemA()
        self.subsystem_b = SubSystemB()
        self.subsystem_c = SubSystemC()
        
    def operation(self):
        results = []
        results.append(self.subsystem_a.operation_a1())
        results.append(self.subsystem_b.operation_b1())
        results.append(self.subsystem_c.operation_c1())
        results.append(self.subsystem_a.operation_a2())
        results.append(self.subsystem_b.operation_b2())
        results.append(self.subsystem_c.operation_c2())
        return "\n".join(results)
    
# client

def client_code(facade: Facade):
    print(facade.operation())
    
# usage
facade = Facade()
client_code(facade)