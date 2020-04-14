# 选择单链表成为队列的数据结构
from linkedlist.single_list import LinkedList


class Queue(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.__item_link_list = LinkedList()

    def __len__(self):
        return len(self.__item_link_list)

    def push(self, value):
        """队列头部添加元素"""
        if len(self) >= self.maxsize:
            raise Exception('队列已满')
        return self.__item_link_list.append(value)

    def pop(self):
        """"队列尾部删除元素"""
        if len(self) <= 0:
            raise Exception('空队列')
        return self.__item_link_list.popleft()
