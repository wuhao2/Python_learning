# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/27 18:49'
"""
求两个链表交叉的节点，思路是如果两个链表等长的话，那么我们只需依次遍历比较这两个链表的节点是否相同即可，
所以如果不等长的话，我们将长的链表多出的节点先遍历过，然后再比较即可
"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def getIntersectionNode(headA, headB):
    if headA is None or headB is None:
        return None
    lenA, lenB = 0, 0
    curA, curB = headA, headB
    while curA:
        lenA += 1
        curA = curA.next
    while curB:
        lenB += 1
        curB = curB.next
    if lenA > lenB:
        for i in range(lenA-lenB):
            headA = headA.next
    if lenA < lenB:
        for i in range(lenB-lenA):
            headB = headB.next
    while headA:
        if headA == headB:
            return headA
        headA = headA.next
        headB = headB.next
    return None


