class Node(object):
    """双向链表节点"""
    __slots__ = ('value', 'prev', 'next')

    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next


class DoubleLinkedList(object):
    """
    双向链表
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        """
        双向链表添加尾节点
        """
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('双向链表已满')
        node = Node(value)
        if self.tailnode is None:
            self.root.next = node
            self.tailnode = node
            self.tailnode.prev = self.root
        else:
            self.tailnode.next = node
            node.prev = self.tailnode.prev
            self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        """
        双向链表添加头节点
        """
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('双向链表已满')
        node = Node(value)
        if self.root.next is None:
            self.root.next = node
            self.tailnode = node
        else:
            node.next = self.root.next
            self.root.next = node
            node.prev = self.root
        self.length += 1

    def iter_node(self):
        """
        生成节点迭代器
        """
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        if curnode is not None:
            yield curnode

    def __iter__(self):
        """
        生成节点迭代器
        """
        for curnode in self.iter_node():
            yield curnode.value

    def remove(self, node):
        """
        删除节点
        """
        if self.root.next is None:
            raise Exception('双向链表为空')
        if node is self.tailnode:
            prevnode = node.prev
            prevnode.next = None
            self.tailnode = prevnode
        else:
            prevnode = node.prev
            nextnode = node.next
            prevnode.next = nextnode
            nextnode.prev = prevnode

    def iter_node_reverse(self):
        """
        反序循环链表
        """
        if self.tailnode is None:
            return
        while self.tailnode.prev is not self.root:
            yield self.tailnode
            self.tailnode = self.tailnode.prev
        yield self.tailnode


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
        添加尾节点O(1)
        :param value:
        :return:
        """
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('双向循环链表已满')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        """
        添加头节点O(1)
        """
        if self.maxsize is not None and len(self) >= self.maxsize:
            raise Exception('双向链表已满')
        node = Node(value)
        if self.root.next is self.root:
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            headnode = self.root.next
            self.root.next = node
            node.prev = self.root
            node.next = headnode
        self.length += 1

    def remove(self, node):
        """
        删除节点O(1)
        """
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        """
        双向链表反向遍历
        """
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode
