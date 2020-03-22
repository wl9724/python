class Node(object):
    """双向链表节点"""
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class CircularDoubleLinkedList(object):
    """
    双向循环链表
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.prev, node.next = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):
        """
        添加节点O(1)
        :param value:
        :return:
        """
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('双向循环链表已满')
        node = Node(value=value)
        tailnode =self.tailnode() or self.root

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length +=1
