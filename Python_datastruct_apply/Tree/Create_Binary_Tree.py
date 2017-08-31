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


# 前序遍历----递归
def preOrderRecursive(node):
    if node is None:  # 递归出口，如果node没有子节点了，递归停止
        return
    print(node.data, end=' ')
    preOrderRecursive(node.left)  # 递归左子树
    preOrderRecursive(node.right)  # 递归右子树


# 中序遍历----递归
def inOrderRecursive(node):
    if node is None:  # 递归出口，如果node没有子节点了，递归停止
        return
    inOrderRecursive(node.left)  # 递归左子树
    print(node.data, end=' ')
    inOrderRecursive(node.right)  # 递归右子树


# 后序遍历----递归
def postOrderResersive(node):
    if node is None:  # 递归出口，如果node没有子节点了，递归停止
        return
    postOrderResersive(node.left)  # 递归左子树
    postOrderResersive(node.right)  # 递归右子树
    print(node.data, end=' ')


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
    # print(root)
    #  print(root.data)  # A
    # print(root.right)  # C
    # print(root.left)  # B

    preOrderRecursive(root)  # A B D C E G F H I
    print('-------'*5)
    inOrderRecursive(root)   # B D A G E C H F I  递归遍历
    print('-------'*5)
    postOrderResersive(root)  # D B G E H I F C A
    print('-------'*5)
    preOrderIter_stack(root)  # A B D C E G F H I 使用栈回溯迭代，前向遍历
    print('-------'*5)
    levelOrder_deque(root)  # A B C D E F G H I 使用队列 层次遍历


