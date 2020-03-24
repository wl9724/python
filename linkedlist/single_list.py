# 单链表节点
class Node(object):
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        """方便打印节点信息"""
        return '<Node: value: {}, next={}>'.format(self.value, self.next)


# 单链表
class LinkedList(object):
    """
    Node(a,Node(c,d))
    """

    def __init__(self, maxsize=None):
        """
        :param maxsize: int or None
        """
        self.maxsize = maxsize
        self.root = Node()
        self.tailnode = None
        self.length = 0

    def __len__(self):
        return self.length

    def append(self, value):
        """
        追加节点，O(1)
        :param value: 节点的值
        :return:
        """
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception('链表已经达到最大值')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        self.tailnode = node
        self.length += 1

    def appendleft(self, value):
        """
        在链表头部添加节点，O(1)
        :param value: 节点的值
        :return:
        """
        if self.maxsize is not None and self.length >= self.maxsize:
            raise Exception('链表已经达到最大值')
        node = Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.tailnode = node

        headnode = self.root.next
        self.root.next = node
        node.next = headnode
        self.length += 1

    def __iter__(self):
        """
        链表迭代器
        :return:
        """
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        """
        从root节点遍历到tail节点
        :return:
        """
        curnode = self.root.next
        while curnode is not self.tailnode:
            yield curnode
            curnode = curnode.next
        if curnode is not None:
            yield curnode

    def remove(self, value):
        """
        删除值为value的节点O(n)
        :param value:
        :return:
        """
        prevnode = self.root
        for curnode in self.iter_node():
            if curnode.value == value:
                prevnode.next = curnode.next
                if curnode is self.tailnode:  # 更新tailnode节点
                    if prevnode is self.root:
                        self.tailnode = None
                    else:
                        self.tailnode = prevnode
                del curnode
                self.length -= 1
                return 1
            else:
                prevnode = curnode

        return -1

    def find(self, value):
        """
        查找值为value的节点O(1)
        :param value:
        :return: 节点的索引
        """
        index = 0
        for node in self.iter_node():
            if node.value == value:
                return index
            index += 1
        return -1

    def popleft(self):
        """
        删除第一个节点O(1)
        :return: 第一个节点的值
        """
        if self.root.next is None:
            raise Exception('不能从空链表中删除数据')
        headnode = self.root.next
        self.root.next = headnode.next
        self.length -= 1
        value = headnode.value

        if headnode == self.tailnode:
            self.tailnode = None
        del headnode
        return value

    def clear(self):
        """
        清空链表O(n)
        :return:
        """
        for node in self.iter_node():
            del node
        self.root.next = None
        self.tailnode = None
        self.length = 0

    def reverse(self):
        """
        反转链表
        :return:
        """
        curnode = self.root.next
        self.tailnode = curnode
        prevnode = None

        while curnode:
            nextnode = curnode.next
            curnode.next = prevnode

            if nextnode is None:
                self.root.next = curnode

            prevnode = curnode
            curnode = nextnode