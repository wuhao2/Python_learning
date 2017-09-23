# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 22:03'
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoList(self, l1, l2):
        """
        :param l1:
        :param l2:
        :return:
        """
        result = ListNode(0)
        cur = result
        while l1 or l2:
            tmp = ListNode(0)
            if l1 and not l2:
                tmp = l1
                l1 = l1.next
            elif l2 and not l1:
                tmp = l2
                l2 = l2.next
            else:
                if l1.val < l2.val:
                    tmp = l1
                    l1 = l1.next
                else:
                    tmp = l2
                    l2 = l2.next
            cur.next, cur = tmp, tmp
        return result.next

l1 = ListNode(1)
l2 = ListNode(2)
m = Solution()
print(m.mergeTwoList(l1, l2))
