"""
迭代器和生成器是python中2种常用的处理序列数据的工具。
迭代器是一个实现了__iter__()、__next__()方法的对象，用于遍历序列数据。
迭代器提供了一个统一的接口，使得可以对序列进行迭代操作，例如使用 for 循环或者手动调用 next() 函数。
生成器是一种用于生成序列值的迭代器，通过yield关键字来定义或者通过生成器表达式创建。
"""
# 1. 自定义迭代器：迭代器对象实现了迭代器协议，即定义了 __iter__() 和 __next__() 方法。__iter__() 方法返回迭代器自身，而 __next__() 方法返回序列中的下一个元素。
class MyIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = 0

    def __iter__(self):
        return self  # 返回迭代器自身，因为迭代器对象本身就是一个迭代器

    def __next__(self):
        if self.current_value < self.max_value:
            result = self.current_value
            self.current_value += 1
            return result
        else:
            raise StopIteration  # 当达到最大值时，抛出 StopIteration 异常，表示迭代结束

# 使用示例
my_iterator = MyIterator(5)
for value in my_iterator:
    print(value)
    
# 2. 通过列表、元组、集合、字典等可迭代数据结构进行转换
# 示例列表
my_list = [1, 2, 3, 4, 5]

# 使用 for 循环遍历列表元素
for item in my_list:
    print(item)

# 使用迭代器遍历列表元素
iter_obj = iter(my_list)
while True:
    try:
        item = next(iter_obj)
        print(item)
    except StopIteration:
        break

