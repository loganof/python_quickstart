"""
definition:
    为对象提供一个替身或占位符来控制对这个对象的访问。用于多种目的，如延迟加载、访问控制、日志记录等。
steps: 
    1. 创建代理接口
    2. 创建真实主题类：在需要时才创建真实主题对象。
"""

# 代理接口
class Subject:
    def request(self):
        raise NotImplementedError
    
# 真实主题
class RealSubject(Subject):
    def request(self):
        return "RealSubect: Handling request."
    
    
# 代理类
class Proxy(Subject):
    def __init__(self, real_subject: Subject) -> None:
        self._real_subject = real_subject
        
    def request(self):
        if self.check_access():
            result = self._real_subject.request()
            self.log_access()
            return result
        else:
            return "Proxy: Access denied."
        
    def check_access(self):
        # 检查访问权限
        print("Proxy: Checking access prior to firing a real request.")
        return True
    
    def log_access(self):
        # 记录日志访问
        print("Proxy: Logging the time of request.")
        
        
# 客户端
def client_code(subject: Subject):
    print(subject.request())
    

# 使用代理
real_subject = RealSubject()
proxy = Proxy(real_subject)

# 客户端通过代码访问真实主题
client_code(proxy)