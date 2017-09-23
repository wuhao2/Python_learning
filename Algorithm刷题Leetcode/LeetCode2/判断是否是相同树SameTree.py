# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/8 14:39'
"""
Same Tree

这个题的意思非常简单，给定两颗二叉树，判断这两颗二叉树是否相同。树相同包括两点：
一是结构相同，而是值相同。因此我们只需要对两棵树同时遍历)(简单的递归)一遍，
遇到不同（结构不同或者值不同）时则返回False；若遍历一遍之后没有发现不同则说明这两棵树相同。
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif p is None or q is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                if self.isSameTree(p.left, p.left):  # 左---左
                    return self.isSameTree(p.right, q.right)  # 右---右
                else:
                    return False
