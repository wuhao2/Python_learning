# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/8 14:48'
"""
Symmetric Tree

这个题是判断一棵树是不是对称树
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""
构建二叉树
         A
      B            C
         D      E       F
              G       H   I
"""
def createTree():
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']  # 列表解析构造这些节点
    A.left = B   # 够着一个二叉树
    A.right = C

    B.right = D

    C.left = E
    C.right = F

    E.left = G

    F.left = H
    F.right = I
    return A  # 返回根节点


class SymmetricTree(object):

    def isSymmetric(self, root):
        if root is None:
            return True
        else:
            return self.isSameTree(root.left, root.right)  # 递归判断其左子树与右子树是否相同

    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        elif q is None or q is None:
            return False
        else:
            if p.val != q.val:
                return False
            else:
                if self.isSameTree(p.left, q.right):  # 左右
                    return self.isSameTree(p.right, q.left)  # 右左
                else:
                    return False
"""
有代码可知，我们首先把这个树分成左右两颗子树，然后遍历这两颗子树，比较时不再是左边和左边的比，
因为对称，所以比较左子树的左节点和右子树的右节点以及左子树的右节点和右子树的左节点是否相等即可
"""
if __name__ == "__main__":

    root = createTree()  # 返回根节点root
    root1 = createTree()  # 返回根节点root1

    s = SymmetricTree()
    print(s.isSameTree(root, root))  # false
    print(s.isSymmetric(root))  # False