import argparse

# 创建解析器
parser = argparse.ArgumentParser(description="demo")

# 添加参数
# name, age为位置参数，必须按顺序提供
# -c 是可选参数
parser.add_argument("name", type=str, help="name")
parser.add_argument("age", type=int, help="age")
parser.add_argument('-c', '--city', default='unkown', help='your city')

# 解析参数
args = parser.parse_args()

print(f"name: {args.name}, age: {args.age}, city: {args.city}") 




