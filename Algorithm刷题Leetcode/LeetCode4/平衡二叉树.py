# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 13:21'


class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        if root == None:
            return True
        return self.getDepth(root) != -100

    def getDepth(self, root):
        if root == None:
            return 0
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)
        if l == -100 or r == -100 or abs(l - r) > 1:
            return -100
        return 1 + max(l, r)
