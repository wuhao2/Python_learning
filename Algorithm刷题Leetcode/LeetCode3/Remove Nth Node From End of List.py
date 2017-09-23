# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 9:47'
"""
从链表中移除倒数第N个数。思想很简单我就不再赘述了，有一个问题是要想知道倒数，
就要知道链表中总共有多少个元素，这里我是先遍历一遍得到长度，
不知道有没有其他更好的办法。代码如下：
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

def removeNthFromEnd(head, n):
    tmp = head
    Length = 0
    while tmp:
        Length += 1
        tmp = tmp.next
    if n == Length:
        return head.next  # 返回倒数第n个
    tmp = head
    for i in range(Length):
        if i == Length - n -1:  # 找到倒数的第n个节点  i + （n-1） = length
            tmp.next = tmp.next.next  # 删除倒数第n个节点
            break
        tmp = tmp.next
    return head

if __name__ == "__main__":
    head = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # while head:
    #     print(head.val)
    #     head = head.next

    print(removeNthFromEnd(head, 5))