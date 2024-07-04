"""
建造者
1. 定义
    用于构建复杂对象的实例。与直接使用构造函数来创建对象不同，建造者模式将对象的构造过程分离出来，通过一个建造者(Builder)对象逐步构建复杂对象。
2. steps
    1. 建造者接口(Builder)：定义用于创建对象不同部分的方法
    2. 具体建造者(Concrete Builder)：实现建造者接口，具体实现每一步构建对象，最终返回复杂对象。
    3. 指挥者(Director):负责使用建造者来构建复杂对象。指挥者并不直接创建产品，而是指导建造者逐步构建产品。
    4. 产品(product):最终构建的复杂对象。
3. advantage
    1. 更好地控制对象创建过程
    2. 提高代码的可读性和可维护性
    3. 支持不同的建造过程
4. 缺点
    1. 更多的代码量：更多的类和代码
    2. 不适用于简单对象
"""

# 产品类
class Product:
    def __init__(self) -> None:
        self.part_a = None
        self.part_b = None
        self.part_c = None
        
    def __str__(self) -> str:
        return f"Product(part={self.part_a}, part_b={self.part_b}, part_c={self.part_c})"
    
    
# 建造者接口
class Builder:
    def build_part_a(self):
        raise NotImplementedError
    
    def build_part_b(self):
        raise NotImplementedError
    
    def build_part_c(self):
        raise NotImplementedError
    
    def get_result(self):
        raise NotImplementedError


# 具体建造者
class ConcreteBuilder(Builder):
    def __init__(self) -> None:
        self.product = Product()
        
    def build_part_a(self):
        self.product.part_a = 'Part A'
        
    def build_part_b(self):
        self.product.part_b = 'Part B'
        
    def build_part_c(self):
        self.product.part_c = 'Part C'
        
    def get_result(self):
        return self.product
    
# 指挥者
class Director:
    def __init__(self, builder: Builder) -> None:
        self.builder = builder
    
    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()
        
# 使用建造者创建产品
builder = ConcreteBuilder()
director = Director(builder)
director.construct()

# 获取最终产品
product = builder.get_result()
print(product)