"""
Any():python内置函数，用于检查可迭代对象中的元素是否至少有一个为真(即不为False,None,0,空字符串, 空列表等)。如果找到一个真值，返回True,否则返回False.
"""

values = [0, 1, 2, 3]
result = any(values)
print(result)

result = any(x % 2 == 0 for x in range(10))
print(result)