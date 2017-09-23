# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 18:02'


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLink(object):
    def __init__(self):
        self.head = None

    '''获取链表的长度'''

    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    '''获取节点'''

    def get(self, index):
        index = index if index > 0 else len(self) + index
        if len(self) < index or index < 0:  # 索引不能越界
            return None
        pre = self.head
        while index:  # 反正就是先定义一个指针指向head，向下寻找，循环条件index--
            pre = pre.next
            index -= 1
        return pre

    '''设置节点'''

    def set(self, index, data):
        node = self.get(index)
        if node:
            node.data = data
        return node

    """尾部添加节点"""

    def addNode(self, data):
        node = Node(data)
        pre = self.head  # 定义一个临时变量pre
        if self.head is None:
            self.head = node
        else:
            while pre.next:
                pre = pre.next
            pre.next = node  # 插入

    def show(self):
        pre = self.head
        while pre:
            if pre.next:
                print(pre.data, "--->", end='')
            else:
                print(pre.data)
            pre = pre.next

    def length(self):
        count = 0
        pre = self.head
        while pre:
            pre = pre.next
            count += 1
        return count

    def isEmpty(self):
        if not self.head:
            print("this is a empty linklist")
            return True
        else:
            print("exist node count is:", self.length())
            return False

    """翻转链表"""

    def reverseLoop(self, head):
        if not head or not head.next:
            return head
        pre = None
        while head:
            Pnext = head.next  # 缓存当前节点的向后指针，待下次迭代用
            head.next = pre  # 这一步是反转的关键，相当于把当前的向前指针作为当前节点的向后指针
            pre = head  # 作为下次迭代时的（当前节点的）向前指针
            head = Pnext  # 作为下次迭代时的（当前）节点
        return pre  # 返回头指针，头指针就是迭代到最后一次时的head变量（赋值给了pre）

    def showReverse(self):
        head = singleLink.head  # 定义一个头指针
        newhead = singleLink.reverseLoop(head)
        while newhead:
            if newhead.next:
                print(newhead.data, "---->", end='')
            else:
                print(newhead.data)
            newhead = newhead.next

    '''根据索引值插入节点'''

    def insert(self, index, data):
        new_node = Node(data)  # 实例化一个节点

        if abs(index + 1) > len(self):  # 索引包括正负值
            return False
        if index >= 0:  # index为负数时
            index = index
        else:  # index为负数时
            index = len(self) + index + 1

        if index == 0:  # 插入到链表头部
            self.head = new_node
            new_node.next = self.head

        else:
            pre = self.get(index - 1)  # 获得一个节点
            if pre:
                '''单链表三步插入: '''
                pre_next_node = pre.next  # 用一个临时变量保存当前节点的后一个节点

                pre.next = new_node  # 指向新节点
                new_node.next = pre_next_node  # 新节点的next指向pre_next_node
            else:
                return False
        return new_node

    '''删除节点'''

    def delete(self, index):
        f = index if index > 0 else abs(index + 1)
        if f > len(self):
            return False  # 索引值不能越界
        pre = self.head
        index = index if index >= 0 else len(self) + index
        prep = None
        while index:
            prep = pre
            pre = pre.next
            index -= 1
        # if prep == None:
        if prep is None:
            self.head = pre.next
        else:
            prep.next = pre.next  # 删除的关键
        return pre.data

    '''清空链表'''

    def clear(self):
        self.head = None
        return True


"""合并两个链表"""


def merge_lists(h1, h2):
    # a 和 b 有一个为空时
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if (h1.data < h2.data):
        h1.next = merge_lists(h1.next, h2)
        return h1
    else:
        h2.next = merge_lists(h2.next, h1)
        return h2


if __name__ == "__main__":
    singleLink = SingleLink()
    singleLink.addNode(1)
    singleLink.addNode(2)
    singleLink.addNode(3)
    singleLink.addNode(4)

    singleLink.insert(2, 8)
    singleLink.insert(3, 9)
    singleLink.delete(2)
    singleLink.show()
    singleLink.isEmpty()
    singleLink.showReverse()
    # print(singleLink.clear())
    #############################################
    singleLink2 = SingleLink()
    singleLink2.addNode(1)
    singleLink2.addNode(2)
    singleLink2.addNode(3)
    singleLink2.addNode(4)

    singleLink2.insert(2, 8)
    singleLink2.insert(3, 9)
    singleLink2.delete(3)
    singleLink2.show()
    singleLink2.isEmpty()
    singleLink2.showReverse()

    # merge_lists(singleLink, singleLink2)