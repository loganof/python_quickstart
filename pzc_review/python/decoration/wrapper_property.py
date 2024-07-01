class Rectangle:
    def __init__(self, width, heigth):
        self._width = width
        self._height = heigth

    # 使用@property装饰器将area方法转换成属性，使我们访问属性一样访问方法，而不需要括号。
    # 作用：使得代码更加简洁和易读
    @property
    def area(self):
        return self._width * self._height

rectangle = Rectangle(3, 2)
print(rectangle.area)