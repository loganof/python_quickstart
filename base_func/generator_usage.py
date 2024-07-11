
"""
1. 生成器（Generator）是一种特殊的迭代器，它允许按需产生值，而不需要一次性将所有值存储在内存中。
2. 生成器通常是通过生成器函数（Generator function）来创建的，生成器函数使用 yield 关键字来产生值，而不是使用 return 返回值。
3. 由于生成器是惰性求值的，因此它只在需要时才生成值，而不是一次性生成所有值。这使得生成器非常适合处理大量数据或者无限序列。
"""

def my_generator(max_value):
    current_value = 0
    while current_value < max_value:
        yield current_value  # 使用 yield 语句产生值
        current_value += 1

# 使用示例
generator = my_generator(5)
for value in generator:
    print(value)

# 通过生成器实现斐波那契数列
import sys
def fibonacci(n):
    a, b, counter = 0, 1, 0
    while True:
        if(counter > n):
            return
        yield a
        a, b = b, a + b
        counter += 1

f = fibonacci(10)# f是一个迭代器，由生成器返回
while True:
    try:
        print(next(f), end=" ")
    except StopIteration:
        sys.exit()

