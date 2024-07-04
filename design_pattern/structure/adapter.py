"""
definition: 
    通过引入一个适配器类，封装原有类的接口，使其符合目标接口的要求，使接口不兼容的类可以协同工作。
steps:
    1. 目标接口(target interface):期望客户端使用的接口。
    2. 适配器(adapter): 实现目标接口。
    3. 适配者(adaptee): 需要被适配的现有类，其接口与目标接口不兼容。
    4. 客户端(client)
"""

# 目标接口
class Target:
    def request(self):
        raise NotImplementedError
    
# 适配者
class Adaptee:
    def specific_request(self):
        return "Adaptee's specific request"
    
    
# 适配器
class Adapter(Target):
    def __init__(self, adaptee: Adaptee) -> None:
        self.adaptee = adaptee
        
    def request(self):
        return self.adaptee.specific_request()
    
    
# 客户端
def client_code(target: Target):
    print(target.request())
    
# 使用适配器
adaptee = Adaptee()
adapter = Adapter(adaptee)

client_code(adapter)
    
    
# 
