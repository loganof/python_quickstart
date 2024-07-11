"""
definition:
    在不破坏封装的情况下捕获和保存对象的内部状态，以便以后恢复该状态。该模式的关键在于，它允许将对象状态保存在备忘录对象中，并在需要时恢复。
structure:
    1. Originator(发起人): 原始对象，其内部状态需要被保存和恢复；提供创建备忘录和从备忘录恢复状态的方法。
    2.Memento(备忘录)：存储Originator的内部状态。备忘录的内容对于其他对象是不可变的。
    3. Caretacker(管理者)：负责保存备忘录，但不能对备忘录的内容进行操作或访问。
"""

# 保存创建备忘录和恢复状态的方法
from typing import List


class Originator:
    def __init__(self, state) -> None:
        self._state = state
        
    def save_state(self):
        return Memento(self._state)
    
    def restore_state(self, memento: "Memento"):
        self._state = memento.get_state()
        
    def set_state(self, state):
        self._state = state
        
    def __str__(self) -> str:
        return f"Originator state: {self._state}"
        
    
    
# Memento:只存储状态并获取状态的方法
class Memento:
    def __init__(self, state) -> None:
        self._state = state
        
    def get_state(self):
        return self._state
    
# Caretaker：保存和恢复备忘录， 但不操作备忘录内容
class Caretaker:
    def __init__(self, originator: Originator) -> None:
        self._originator = originator
        self._history : List[Memento]= []
        
    def backup(self):
        self._history.append(self._originator.save_state())
        
    def undo(self):
        if not self._history:
            return
        memento = self._history.pop()
        self._originator.restore_state(memento)
    
    def show_history(self):
        for memento in self._history:
            print(f"Memento state: {memento.get_state()}")
            
            
# usage
originator = Originator("State1")
caretaker = Caretaker(originator)

# save state
caretaker.backup()
print(originator)

# change state and save
originator.set_state("State2")
caretaker.backup()
print(originator)

# change state 
originator.set_state("State3")
print(originator)

caretaker.undo()
print(originator)

caretaker.undo()
print(originator)

# show history 
caretaker.show_history()