class MyClass:
    @staticmethod
    def static_method(x, y):
        return x + y
    
# 通过类名调用
result = MyClass.static_method(3, 5)
print(result)

# 通过实例调用
obj = MyClass()
result = obj.static_method(2, 5)
print(result)