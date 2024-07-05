"""
definition: 
    它定义了一系列算法，并将算法封装起来，使它们可以相互替换。
structure: 
    1. Context(上下文):
    2. Strategy(策略):策略接口，所有具体策略都实现该接口。
    3. ConcreteStrategy(具体策略):实现策略接口的具体算法。
"""

from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError
    
# 具体策略A
class ConcreteStrategyA(Strategy):
    def execute(self, data):
        return sorted(data)


# 具体策略B
class ConcreteStrategyB(Strategy):
    def execute(self, data):
        return sorted(data, reverse=True)
    
    
# 具体策略C
class ConcreteStrategyC(Strategy):
    def execute(self, data):
        return data
    
    
# 上下文 
class Context:
    def __init__(self, strategy: Strategy) -> None:
        self._strategy = strategy
        
    def set_strategy(self, strategy: Strategy):
        self._strategy = strategy
        
    def do_something(self, data):
        return self._strategy.execute(data)
    
# 使用示例
data = [5, 2, 9, 1]

context = Context(ConcreteStrategyA())
print("ConcreteStrategyA:", context.do_something(data))

context.set_strategy(ConcreteStrategyB())

print("ConcreteStrategyB:", context.do_something(data))

context.set_strategy(ConcreteStrategyC())
print("ConcreteStrategyC:", context.do_something(data))

