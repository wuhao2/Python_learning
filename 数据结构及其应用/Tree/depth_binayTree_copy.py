# 构建树节点
class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        # None表示如果不传左右节点，即表示这个没有左右节点
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


# 构建二叉树
def createTree():
    A, B, C, D, E, F, G, H, I = [TreeNode(x) for x in 'ABCDEFGHI']
    A.left = B
    A.right = C
    B.right = D
    C.left = E
    C.right = F
    E.left = G
    F.left = H
    F.right = I
    return A  # 返回根节点
'''
递归求二叉树的深度
'''
def depth(node):
    if node is None:  # 递归出口
        return 0  # 空树，深度为0
    dl = depth(node.left)  # 左子树深度
    dr = depth(node.right)  # 右子树深度
    return max(dl, dr) + 1


'''
非递归求二叉树的深度
'''
from collections import deque
# 层序遍历二叉树的各个节点
def depth2(root):
    q = deque([(root, 1)])  # 传入一个元组，用来记录二叉树的层
    while q:
        node, d = q.popleft()  # 出队列，元组拆包
        print(node, end=" ")
        if node.left:
            q.append((node.left, d+1))  # 入队左孩子
        if node.right:
            q.append((node.right, d+1))  # 入队右孩子
    return d  # d就是最后一个节点所在的层


'''
拷贝二叉树
'''
def copyTree(node):
    if node is None:
        return None
    left = copyTree(node.left)
    right = copyTree(node.right)
    return TreeNode(node.data, left, right)


if __name__ == '__main__':
    root = createTree()
    print(depth(root))  # 4层
    print(depth2(root))  # 4层

    # newTree = copyTree(root)
    # print(depth(newTree))  # 4层
    # print(depth2(root))  # 4层