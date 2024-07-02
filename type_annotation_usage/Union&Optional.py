from typing import Union

# Union 表示变量可以是指定类型中的任意一个
def process(data: Union[int, str]) -> None:
    if isinstance(data, int):
        print(f"Processing integer: {data}")
    elif isinstance(data, str):
        print(f"Processing string: {data}") 
        
# Optional是Union的一种特殊情况，它表示一个变量可以是某个指定类型或None
# Optional[X], 等同于Union[X, None]   

from typing import Optional
def greet(name: Optional[str]) -> str:
    if name is None:
        return "Hello, guest!"
    else:
        return "Hello, " + name + "!"   