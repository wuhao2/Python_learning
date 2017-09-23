# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 15:40 '

'''创建节点Node'''


class Node(object):
    def __init__(self, data):
        self.data = data  # 数据域
        self.next = None  # 指针域


'''创建链表(单向链表的实现）'''


class Linklist(object):
    def __init__(self):
        self.head = None  # 头指针指向空

    '''获取链表的长度'''

    def __len__(self):
        pre = self.head
        length = 0
        while pre:
            length += 1
            pre = pre.next
        return length

    '''判断链表是否为空'''

    def isEmpty(self):
        return False if len(self) > 0 else True

    ''' 从尾部追加节点'''

    def append(self, data):
        node = Node(data)
        pre = self.head  # 定义一个指针指针指向链表头指针
        if self.head is None:
            self.head = node
        else:
            while pre.next:
                pre = pre.next  # 找到末尾
            pre.next = node  # 将节点追加到末尾

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

    '''插入节点'''

    def insert(self, index, data):
        node = Node(data)  # 实例化一个节点

        if abs(index + 1) > len(self):  # 索引包括正负值
            return False
        if index >= 0:  # index为负数时
            index = index
        else:  # index为负数时
            index = len(self) + index + 1

        if index == 0:  # 插入到链表头部
            self.head = node
            node.next = self.head

        else:
            pre = self.get(index - 1)  # 获得前一个节点
            if pre:
                '''单链表三步插入: '''
                pre_next_node = pre.next  # 单链表三步插入
                pre.next = node
                node.next = pre_next_node
            else:
                return False
        return node

    '''删除节点'''

    def delete(self, index):
        f = index if index > 0 else abs(index + 1)
        if f > len(self):
            return False
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

    '''打印链表'''

    def show(self):
        pre = self.head
        while pre:
            print(pre.data)
            pre = pre.next
        print()

    '''遍历链表'''

    def view(self):
        Node = self.head
        linkstr = ""
        while Node is not None:
            if Node.next is not None:
                linkstr = linkstr + str(Node.data) + "-->"  # 节点与节点之间用箭头连接
            else:
                linkstr += str(Node.data)  # 最后一个节点，不需要--->
            Node = Node.next  # 将指针移至下一个节点
        print(linkstr)

    '''反转链表'''

    def __reversed__(self):
        def reverse(pre_node, node):
            if pre_node is self.head:
                pre_node.next = None
            if node:
                next_node = node.next
                node.next = pre_node
                return reverse(node, next_node)
            else:
                self.head = pre_node
            return reverse(self.head, self.head.next)


if __name__ == '__main__':
    ls = Linklist()
    ls.append(1)
    ls.append(2)
    ls.append(3)
    ls.insert(-1, 10)
    ls.view()
    print("get node data: ", ls.get(-1).data)

    print(ls.delete(1))
    print('after delete:')
    ls.view()

    ls.set(-1, 20)
    print("after set: ")
    ls.view()

    reversed(ls)
    print('after reverse linklist: ')
    ls.view()

    print('after get: ')
    print(ls.get(1).data)
    ls.view()
