# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/8 15:03'
"""
Add Two Numbers

这个题目是实现链表的加法，刚开始理解错了，看到题目给的例子以为给的两个列表长度是相等的，
其实不是哈，不一定等长。题目本身很简单，值得一提的是python中链表的操作
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    def addTwoNumber(self, l1, l2):
        add = 0
        l3 = ListNode(0)
        cur = l3
        while l1 or l2:
            node = ListNode(add)
            if l1:
                node.val += l1.val
                l1 = l1.next
            if l2:
                node.val += l2.val
                l2 = l2.next
            if node.val >= 10:
                add = 1
            else:
                add = 0
            node.val %= 10
            cur.next, cur = node, node
        if add:
            cur.next = ListNode(1)
        return l3.next

if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(1)
    s = Solution()
    print(s.addTwoNumber(node1, node2))
