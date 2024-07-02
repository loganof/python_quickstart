def print_and_return(string):
    print(string)
    return string  

def format_str(count, val, nwords):
    return(f"word list has {count} occurrences of {val}, out of {nwords} words")

dsk = {
    "word": 'apple orange banana apple orange apple',   
    "nwords": (len, (str.split, 'words')),
    "val1": 'orange',
    'val2': 'apple',
    'val3': 'pear',
    'count1': (str.count, 'word', 'val1'),  
    'count2': (str.count, 'word', 'val2'),  
    'count3': (str.count, 'word', 'val3'),  
    'format1': (format_str, 'count1', 'val1', 'nwords'),    
    'format2': (format_str, 'count2', 'val2', 'nwords'),  
    'format3': (format_str, 'count3', 'val3', 'nwords'),  
    'print1': (print_and_return, 'format1'),    
    'print2': (print_and_return, 'format2'),        
    'print3': (print_and_return, 'format3')
}

from dask.threaded import get
from dask.optimization import cull

outputs = ['print1', 'print2']
dsk1, dependencies = cull(dsk, outputs)
results = get(dsk1, outputs)
print(results)
