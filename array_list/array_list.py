# 实现一个定长的数组
class Array(object):

    def __init__(self, size=None):
        self._size=size
        self._items = [None]*size

    def __getitem__(self, index):
        if index >= self._size:
            raise Exception('index not find')
        return self._items[index]

    def __setitem__(self, index, value):
        if index >= self._size:
            raise Exception('index not find')
        self._items[index] = value

    def __len__(self):
        return self._size

    def clear(self, value=None):
        for i in range(len(self._items)):
            self._items[i] = value

    def __iter__(self):
        for item in self._items:
            yield item
