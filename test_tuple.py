from filecmp import cmp
from typing import Tuple

# empty tuple
tp = ()
print(tp)
tp = tuple(())
print(tp)

# single element
# tp2 = (1) # error
tp2 = (1,)
print(tp2)
tp2 = tuple((1,))
print(tp2)

# multiple elements
tp3 = (1, 2, 3)
print(tp3)
tp3 = tuple((1, 2, 3))
print(tp3)

tp4 = tp3 + tp3
print(tp4)


# tuple definition in function
def func(tp: Tuple[int, int]):
    print(tp)
func((5, 6))

print(min(tp3))
print(max(tp3))
print(len(tp3))
