# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 22:34'


class SingleNode(object):
    """单链表的结点"""

    def __init__(self, item):
        # _item存放数据元素
        self.item = item
        # _next是下一个节点的标识
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self._head = node
        if node:
            node.next = node  # 指向自己

    def is_empty(self):
        """判断链表是否为空"""
        return self._head is None

    def length(self):
        """链表长度"""
        if self.is_empty():
            return 0
        # cur初始时指向头节点
        cur = self._head
        count = 1
        # 尾节点指向None，当未到达尾部时
        while cur.next != self._head:
            count += 1
            # 将cur后移一个节点
            cur = cur.next
        return count

    def travel(self):
        """遍历链表"""
        if self.is_empty():
            return 0
        cur = self._head  # 游标
        while cur.next != self._head:
            print(cur.item, end=" ")
            cur = cur.next
        # 退出循环cur指向尾节点，但尾节点的数据没有打印
        print(cur.item)

    def add(self, item):
        """头部添加元素  O(1)"""
        # 先创建一个保存item值的节点
        node = SingleNode(item)
        if self.is_empty():  # 特殊情况
            self._head = node
            node.next = node

        cur = self._head  # 游标 指向_head所指向的头结点
        while cur.next != self._head:
            cur = cur.next  # 找到尾节点
        node.next = self._head  # 将新节点的链接域next指向头节点，即_head指向的位置
        self._head = node  # 将链表的头_head指向新节点
        cur.next = node  # 因为是循环链表所以尾节点的next指向头结点

    def append(self, item):
        """尾部添加元素   O(n)"""
        node = SingleNode(item)
        # 先判断链表是否为空，若是空链表，则将_head指向新节点
        if self.is_empty():
            self._head = node
            node.next = node

        # 若不为空，则找到尾部，将尾节点的next指向新节点
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            cur.next = node  # 尾插
            node.next = self._head  # 将尾插节点的next指向头节点

    def insert(self, pos, item):
        """指定位置添加元素   最坏情况为O(n)"""
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos > (self.length() - 1):
            self.append(item)
        # 找到指定位置
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头节点开始移动到指定位置
            pre = self._head
            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 先将新节点node的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self, item):
        """删除数据为item的节点"""
        if self.is_empty():  # 特殊情况@1
            return
        cur = self._head
        pre = None
        while cur.next != self._head:
            # 找到了指定元素
            if cur.item == item:

                if cur == self._head:  # 特殊情况@2 如果第一个头节点就是删除的节点
                    # 将头指针指向头节点的后一个节点
                    tail = self._head  # 定义一个游标，去寻找尾节点
                    while tail.next != self._head:
                        tail = tail.next

                    self._head = cur.next  # 删除头节点
                    tail.next = self._head  # 将尾节点的next指向新的头节点
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                return
            else:
                # 继续按链表后移节点
                pre = cur
                cur = cur.next
        # 特殊情况@3 退出循环时，没有比较最后一个节点，此处需要在比较一次
        if cur.item == item:
            if cur == self._head:  # 特殊情况@4  链表只有一个节点
                self._head = None
            pre.next = cur.next

    def search(self, item):
        """链表查找节点是否存在，并返回True或者False"""
        if self.is_empty():
            return False
        cur = self._head
        while cur.next != self._head:
            if cur.item == item:
                return True
            cur = cur.next
        if cur.item == item:  # 退出循环时，没有比较最后一个节点，此处需要在比较一次
            return True
        return False


if __name__ == "__main__":
    ll = SingleLinkList()
    ll.add(1)
    ll.add(2)
    ll.add(5)
    ll.add(9)
    ll.append(3)
    ll.append(8)
    ll.insert(2, 4)

    print("length:", ll.length())
    ll.travel()

    print(ll.search(3))
    print(ll.search(5))

    print("delete 1:")
    ll.remove(1)
    ll.travel()

    print("delet 9:")
    ll.remove(9)
    ll.travel()

    print("length:", ll.length())
    ll.travel()
