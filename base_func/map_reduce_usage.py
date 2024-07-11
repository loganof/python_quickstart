"""
map():将函数应用于一个或多个可迭代对象(如列表)的每个元素，并返回一个新的迭代器。
reduce(): 对可迭代对象进行累积计算。将前两个元素应用于函数，然后将结果与下一个元素一起作用于函数，依次类推，直到处理完所有的元素。
"""

# map

# function
def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = map(square, numbers)
print(list(squared_numbers))

# lambda
squared_numbers = map(lambda x: x * x, numbers)
print(set(squared_numbers))

# 多个表达式
numbers2 = [6, 7, 8, 9, 10]
summed_numbers = map(lambda x, y: x + y, numbers, numbers2)
print(list(summed_numbers))

# reduce
from functools import reduce

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)

print(sum_of_numbers)