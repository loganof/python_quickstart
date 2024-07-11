"""
35 keywords
1. from, import, as (3)
2. def, class, async, await, yield, return, pass, lambda (8)
3. if, else, elif, while, continue, break, for, in (8)
4. and, or, is, not, True, False, None(7)
5. try, except, finally, assert, raise(5)
6. with, del, nonlocal, global

"""

# list keywords
import keyword
print(keyword.kwlist)

# nonlocal usage
def outer_function():
    x = 10
    def inner_function():
        nonlocal x
        x = 20
        
    inner_function()
    print(x)
    
outer_function()
