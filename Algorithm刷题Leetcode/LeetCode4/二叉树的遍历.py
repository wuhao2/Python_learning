# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 10:26'
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

# 前序遍历----因为递归开销太大，使用stack迭代进行----使用栈
def preOrderIter_stack(root):
    s = []  # 运用栈的回溯
    node = root
    while True:
        while node:  # 把node都压栈，直到node为空
            print(node, end=' ')  # 访问root或者子
            s.append(node)  # 压栈
            node = node.left  # 访问左子树（）

        if not s:  # 如果栈为空，就不能回溯了
            break
        node = s.pop().right  # 先回溯，然后访问右子树（）


from collections import deque
# 层序遍历二叉树的各个节点----使用队列-----先进先出
def levelOrder_deque(root):
    q = deque([root])  # 初始化时只，将根节点放入队列中
    while q:
        node = q.popleft()  # 从左边出队列
        print(node, end=' ')  # 输出

        if node.left:
            q.append(node.left)  # 入队左孩子
        if node.right:
            q.append(node.right)   # 入队右孩子

# 测试
if __name__ == '__main__':
    root = createTree()  # 返回根节点A
    levelOrder_deque(root)
    print()
    preOrderIter_stack(root)
