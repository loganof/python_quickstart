"""
definition:
    定义一个对象（中介者）来封装一组对象之间的交互方式。这样对象之间的直接交互被中介者所替代。通过中介者实现各个对象的解耦和独立。
    
structure:
    1. Mediator
    2. ConcreteMediator
    3. Colleague
    4. ConcreteColleague
"""

# 中介者接口
class Mediator:
    def notify(self, sender, event):
        pass
    
class ConcreteMeditor(Mediator):
    def __init__(self) -> None:
        self._colleague1 = None
        self._colleague2 = None
        
    def set_colleague1(self, colleague: "Colleague"):
        self._colleague1 = colleague
        
    def set_colleague2(self, colleague: "Colleague"):
        self._colleague2 = colleague
        
    def notify(self, sender, colleague: "Colleague"):
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._colleague2.do_c()
            
        elif event == "B":
            print("Mediator reacts on B and triggers following operations:")
            self._colleague1.do_a()
            self._colleague2.do_c()
            
# 同事抽象类
class Colleague:
    def __init__(self, mediator: Mediator) -> None:
        self._mediator: Mediator = mediator
        
        
# 具体同事1
class ConcreteColleague1(Colleague):
    def do_a(self):
        print("Colleague1 does A.")
        self._mediator.notify(self, "A")
        
    def do_b(self):
        print("Colleague1 does B.")
        self._mediator.notify(self, "B")
        
    def do_d(self):
        print("Colleague1 does D.")
        self._mediator.notify(self, "D")
        
class ConcreteColleague2(Colleague):
    def do_c(self):
        print("Colleague2 does C.")
    def do_d(self):
        print("Colleague2 does D.")
        
# 使用示例
mediator = ConcreteMeditor()
colleague1 = ConcreteColleague1(mediator)
colleague2 = ConcreteColleague2(mediator)

mediator.set_colleague1(colleague1)
        
        
