# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/7 21:42'
# 构建树节点
class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        # None表示如果不传左右节点，即表示这个没有左右节点
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

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

def preOrderRecursive(root):
    if root is None:
        return
    else:
        print(root.data, "--->", end='')
        preOrderRecursive(root.left)
        preOrderRecursive(root.right)

"""使用栈实现深度优先遍历dfs----前序遍历"""
def preOrderStack(root):
    res = []
    currentNode = root
    while currentNode:
        print(currentNode.data, "--->", end='')
        if currentNode.right:
            res.append(currentNode.right)  # 将当前节点的有节点入栈
        if currentNode.left:
            currentNode = currentNode.left  # 一直往左走
        else:
            if not res:  # 当栈为空时，将当前节点置为空， 退出while循环
                currentNode = None
            else:
                currentNode = res.pop()

"""使用队列实现广度优先遍历bfs ---逐层遍历"""
from collections import deque
def levelOrderQueue(root):
    q = deque([root])
    while q:
        node = q.popleft()
        print(node.data, "--->", end='')
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)

# 测试
if __name__ == '__main__':
    root = createTree()  # 返回根节点A
    preOrderRecursive(root)
    print()
    preOrderStack(root)
    print()
    levelOrderQueue(root)

"""
result:
A --->B --->D --->C --->E --->G --->F --->H --->I --->
A --->B --->D --->C --->E --->G --->F --->H --->I --->
A --->B --->C --->D --->E --->F --->G --->H --->I --->
"""