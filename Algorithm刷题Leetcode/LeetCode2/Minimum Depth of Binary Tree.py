# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/12 14:48'

def minDepth(root):
    if root is None:
        return 0
    if root.left is None or root.right is None:
        return 1
    left = right = float("inf")  # 无穷大
    if root.left is not None:
        left = 1 + minDepth(root.left)
    if root.right is not None:
        right = 1 + minDepth(root.right)
    return min(left, right)


def maxDepth(self, root):
    if root is None:
        return 0  # 空树
    if root.left is None and root.right is None:
        return 1  # 只有一个根节点
    left = right = -1
    if root.left is not None:
        left = 1 + self.maxDepth(root.left)
    if root.right is not None:
        right = 1 + self.maxDepth(root.right)
    return max(left, right)