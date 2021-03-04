"""
Write your own iterator (implement it with the __next__ and __iter__ methods)
so that when looping through the loop, it returns only elements at even indices squared.
"""


class MyIterator:
    def __init__(self, collection, cursor):
        self._collection = collection
        self._cursor = cursor

    def __next__(self):
        if self._cursor + 1 >= len(self._collection):
            raise StopIteration()
        self._cursor += 1
        if self._cursor % 2:
            return self._collection[self._cursor ] ** 2
        else:
            return '\b'



class ListCollection:
    def __init__(self, collection):
        self._collection = collection

    def __iter__(self):
        return MyIterator(self._collection, -1)

_iterable = ListCollection([1, 2, 3, 4, 5, 6])
for i in _iterable:
    print(i)