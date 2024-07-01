# Refer to README for detailed instructions.

from __future__ import print_function


class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail


def cons(head, tail=None):
    return LinkedList(head, tail)


def listToString(list):
    if list is None:
        return ""
    if list.tail is None:
        return str(list.head)
    return str(list.head) + " " + listToString(list.tail)


def myMap(fn, list):
    if list is None:
        return None
    return cons(fn(list.head), myMap(fn, list.tail))


def myReduce(fn, accm, list):
    if list is None:
        return accm
    return myReduce(fn, fn(accm, list.head), list.tail)


def myReduceRight(fn, accm, list):
    # [BEGIN] YOUR CODE HERE
    # when list is None
    if list is None:
        return accm
    # when traversing to the last node
    if list.tail is None:
        return fn(list.head, accm)
    # [END] YOUR CODE HERE
    return fn(list.head, myReduceRight(fn, accm, list.tail))


def myMap2(fn, list):
    # [BEGIN] YOUR CODE HERE
    import types
    def delayFn(cur, acc: LinkedList):
        newList = cons(None)
        newList.tail = acc
        newList.head = lambda: fn(cur)
        return newList

    storeList = myReduceRight(delayFn, None, list)

    def storeFn(store):
        if store is None:
            return None
        # distinguish whether store.head is function
        if isinstance(store.head, types.FunctionType):
            store.head = store.head()
        else:
            store.head = store.head
        store.tail = storeFn(store.tail)
        return store

    # [END] YOUR CODE HERE
    return storeFn(storeList)


def main():
    exampleList = cons(1, cons(2, cons(3, cons(4))))
    plusOne = lambda x: x + 1
    xTimesTwoPlusY = lambda x, y: x * 2 + y
    def printXAndReturnY(x, y):
        print(x)
        return y
    def unfoldCalculation(x, y):
        return "fn(%s, %s)" % (str(x), str(y))
    printAndReturn = print
    print(listToString(exampleList), "should be 1 2 3 4")
    print(listToString(myMap(plusOne, exampleList)), "should be 2 3 4 5")
    print(myReduce(xTimesTwoPlusY, 0, exampleList), "should be 26")
    print(myReduce(unfoldCalculation, "accm", exampleList), "should be fn(fn(fn(fn(accm, 1), 2), 3), 4)")
    print(myReduceRight(xTimesTwoPlusY, 0, exampleList), "should be 20")
    print(myReduceRight(unfoldCalculation, "accm", exampleList), "should be fn(1, fn(2, fn(3, fn(4, accm))))")
    print("Below should output 4 3 2 1 each on a separate line:")
    myReduceRight(printXAndReturnY, 0, exampleList)
    print(listToString(myMap2(plusOne, exampleList)), "should be 2 3 4 5")
    print("The two outputs below should be equal:")
    print("First output:")
    myMap(printAndReturn, exampleList)
    print("Second output:")
    myMap2(printAndReturn, exampleList)


if __name__ == "__main__":
    main()
