import argparse

# 创建解析器
parse = argparse.ArgumentParser(description="demo")

# 添加子命令解析器
subparsers = parse.add_subparsers(dest="command")   

# 添加子命令
parser_greet = subparsers.add_parser("greet", help="打招呼")  
parser_greet.add_argument('name', type=str, help='名字')   
parser_greet.add_argument('-l', '-l-language', type=str, choices=['en', 'es', 'fr'], default='en', help='语言')  
 
parser_cal = subparsers.add_parser("calculate", help="计算")
parser_cal.add_argument('x', type=int, help='第一个数')
parser_cal.add_argument('y', type=int, help='第2个数')
parser_cal.add_argument('-o', '--operation', type=str, choices=['+', '-', '*', '/'], default='+', help='运算符')

# 解析参数
args = parse.parse_args()

if args.command == "greet":
    print(f"Hello, {args.name}!")
elif args.command == "calculate":
    if args.operation == '+':
        print(args.x + args.y)
    elif args.operation == '-':
        print(args.x - args.y)
    elif args.operation == '*':
        print(args.x * args.y)
    elif args.operation == '/':
        print(args.x / args.y)