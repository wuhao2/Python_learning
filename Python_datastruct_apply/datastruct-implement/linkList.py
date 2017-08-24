# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 15:40 '

#创建节点Node
class Node():
    def __init__(self, data):
        self.data = data#初始化节点，只存储数据，不指向任何节点
        self.next = None

#创建链表(单向链表的实现）
class Linklist():
    def __init__(self, Node):
        self.head = Node#头指针指向下一个
        self.head.next = None
        self.tail = self.head#初始化链表，表头和表尾重合

    #从尾部添加节点
    def add(self,Node):
        self.tail.next = Node#将节点挂接
        self.tail = self.tail.next#将表尾后移

    # #从尾部删除节点
    # def delete(self, Node):
    #     self.head =

    #遍历链表
    def view(self):
        Node = self.head
        linkstr = ""
        while Node is not None:
            if Node.next is not None:
                linkstr = linkstr + str(Node.data) + "-->"#节点与节点之间用箭头连接
            else:
                linkstr += str(Node.data)#最后一个节点，不需要--->
            Node = Node.next#将指针移至下一个节点
        print(linkstr)


Node1 = Node(7)
Node2 = Node("wuhao")
Node3 = Node("xiangwen")
Node4 = Node(8)

x = Linklist(Node1)
x.add(Node2)
x.add(Node3)
x.add(Node4)
# x.delete()

x.view()



