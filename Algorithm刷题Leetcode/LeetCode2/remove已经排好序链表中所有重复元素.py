# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/8 15:30'
"""
Remove Duplicates from Sorted List

这个题目的意思是去除掉链表中所有重复的元素，即每个元素只保留一次，方法就是遍历这个链表，
每次将当前节点的值跟下一个的节点的值相比，如果相同则将当前节点指向下下个节点即可，
需要注意的是如果下下个节点没有的话，则当前节点指向None。
"""

# definition for single-linked list
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def __init__(self):
        self.head = None
    """尾部添加节点"""

    def addNode(self, data):
        node = ListNode(data)
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

    def deleteDuplicates(self, head):
        if head is None:
            return None
        else:
            cur = ListNode(head.val)  # 当前节点的值
            cur.next = head, cur
            while cur:
                if cur.next and cur.val == cur.next.val:
                    if cur.next and cur.val:
                        cur.next = cur.next.next
                    else:
                        cur.next = None
                else:
                    cur = cur.next
            return head


if __name__ == "__main__":
    s = Solution()
    s.addNode(0)
    s.addNode(1)
    s.addNode(2)
    s.addNode(3)
    print(s.show())