class Myclass:
    class_attribute = 0
    
    @classmethod
    def class_method(cls):
        cls.class_attribute += 1
        print(f"Class attribute: {cls.class_attribute}")
        
# 通过类名调用
Myclass.class_method()

# 通过实例调用

obj = Myclass()
obj.class_method()  