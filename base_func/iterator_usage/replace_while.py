import sys

f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)
    
    
list = [1, 2, 3, 5]
# 创建迭代器对象
it = iter(list)
print(next(it))
print(next(it))

# 使用for循环遍历
for index in it:
    print(index, end = " ")
    
# 使用while进行遍历
while True:
    try:
        print(next(it))
    except Exception:
        sys.exit()
        