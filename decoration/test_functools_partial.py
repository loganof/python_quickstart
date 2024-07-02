from functools import partial


def spam(a, b, c, d):
    print(a, b, c, d)

func1 = partial(spam, 1)
func1(2,3,4)

func2 = partial(spam, d=3)
func2(1,3,5)
