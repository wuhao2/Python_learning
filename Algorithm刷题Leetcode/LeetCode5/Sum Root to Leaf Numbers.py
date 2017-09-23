# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 15:36'
"""
给定一棵树，从其根节点至其任意一个叶子节点分别代表一个数，求这些数之和。
其实就是遍历这个二叉树，每次遍历的时候把上次的数记下来，在下一次乘10在加起来就可以了
"""

"""
构建二叉树
         A
      B            C
         D      E       F
              G       H   I
"""
def createTree():
    l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in l]  # 列表解析构造这些节点
    A.left = B  # 够着一个二叉树
    A.right = C

    B.right = D

    C.left = E
    C.right = F

    E.left = G

    F.left = H
    F.right = I
    return A  # 返回根节点


# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        sum = 0
        if root is None:
            return sum
        if root.left is None and root.right is None:
            sum += root.val
        if root.left:
            sum += self.sumNumbers1(root.left, 10 * root.val)
        if root.right:
            sum += self.sumNumbers1(root.right, 10 * root.val)
        return sum

    def sumNumbers1(self, root, sum):
        if root is None:
            return sum
        if root.left is None and root.right is None:
            sum += root.val
            return sum
        left = right = 0
        if root.left:
            left = self.sumNumbers1(root.left, 10 * (root.val + sum))
        if root.right:
            right = self.sumNumbers1(root.right, 10 * (root.val + sum))
        sum = left + right
        return sum


# 测试
if __name__ == '__main__':
    root = createTree()  # 返回根节点A
    s = Solution()
    print(s.sumNumbers(root))
