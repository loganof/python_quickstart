"""
definition:
    用于定义对象的一种一对多依赖关系，当一个对象的状态发生改变时，所有依赖它的对象都会得到通知并自动更新。这种模式用于实现分布式事件处理系统。
steps:
    1. Subject(主题/被观察者)
        1. 维护一组观察者并提供添加、删除观察者的方法。
        2. 当自身状态发生变化时，通知所有观察者。
    2. Observer(观察者)
        1. 定义一个更新接口，供主题在其状态发生变化时通知观察者。
    3. ConcreteObserver(具体观察者)
        1. 实现观察者接口，定义响应方法。
usage:
    1. 观察者广泛应用于事件处理系统、订阅-发布模式、模型-视图-控制器(MVC)架构等场景。
"""
from typing import Optional, List

# 观察者接口
class Observer:
    def update(self, state):
        pass


# 具体观察者
class ConcreteObserver(Observer):
    def __init__(self, name) -> None:
        self._name = name
        self._state = None
        
        
    def update(self, state):
        self._state = state
        print(f"Observer {self._name} updated to state: {self._state}")
        
        
# 主题接口
class Subject:
    def __init__(self) -> None:
        self._observers: Optional[List[Observer]] = []
        
    def attach(self, observer: Observer) -> None:
        self._observers.append(observer)
        
    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)
        
        
    def notify(self):
        for observer in self._observers:
            observer.update(self._state)
            
# 具体主题
class ConcreteSubject(Subject):
    def __init__(self) -> None:
        super().__init__()
        self._state = None
        
    def get_state(self):
        return self._state
    
    def set_state(self, state):
        self._state = state
        self.notify()
        

subject = ConcreteSubject()

observer1 = ConcreteObserver("observer1")
observer2 = ConcreteObserver("observer2")

subject.attach(observer1)
subject.attach(observer2)

subject.set_state("State1")
subject.set_state("State2")

subject.detach(observer1)

subject.set_state("State3")