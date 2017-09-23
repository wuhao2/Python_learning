# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 14:19'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def swapPairs(head):
    if head == None or head.next == None:
        return head
    result = ListNode(0)
    result.next, cur = head, result
    while head and head.next:
        cur.next = head.next
        head.next = cur.next.next
        cur.next.next = head
        cur = head
        head = head.next
    return result.next

if __name__ == "__main__":
    head = ListNode(0)
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    swapPairs(head)