# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/27 18:45'
"""
判断一个链表是否有循环，思路是我先建一个节点，然后遍历这个链表，每遍历一个节点，
就让这个节点指向刚刚新建的那个节点，这样如果有循环，那么它回来之后的next就会指向那个节点，那么就代表有循环。
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        tmp = ListNode(0)
        result = False
        if head is None:
            return result
        while head:
            if head.next is None:
                return result
            if head.next == tmp:
                result = True
                return result
            cur, head.next = head.next, tmp
            head = cur