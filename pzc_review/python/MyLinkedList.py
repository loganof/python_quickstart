class Node:
    def __init__(self, item):
        self._item = item
        self._next = None


class LinkedList:
    def __init__(self):
        self._head = None

    def is_empty(self):
        if self._head == None:
            return True
        return False

    def length(self):
        i = 1
        cur = self._head
        while cur._next != None:
            i += 1
            cur = cur._next
        return i

    def add(self, item):
        node = Node(item)
        node._next = self._head
        self._head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self._head = node
        cur = self._head
        while cur._next != None:
            cur = cur._next
        cur._next = node

    def insert(self, pos, item):
        if pos <= 0:
            self.add(item)
        elif pos > self.length() -1:
            self.append(item)

        else:
            pre = self._head
            index = 0
            while index < pos:
                pre = self._head._next
                index += 1
            next = pre._next
            pre._next = Node(item)
            pre._next._next = next



