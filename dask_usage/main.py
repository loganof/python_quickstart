from dask.threaded import get

from operator import add
dsk = {
    'x': 1,
    'y': 2,
    'z': (add, 'x', 'y'),
    'w': (sum, ['x', 'y', 'z'])  
}

print(get(dsk, 'x'))
print(get(dsk, 'z'))

print(get(dsk, 'w'))   
print(get(dsk, ['x', 'y', 'z']))
print(get(dsk, [['x', 'y'],['z', 'w']]))   # 错误 1 修复：将单个列表更改为嵌套列表  