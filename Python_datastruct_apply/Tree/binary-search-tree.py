# 构建树节点
class TreeNode(object):
    def __init__(self, data, left=None, right=None):
        # None表示如果不传左右节点，即表示这个没有左右节点
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    '''
    查找search_data，返回查找到的节点，对外接口
    '''
    def search(self, search_data):
        node, _ = self._search(search_data)
        return node
        # 为了避免代码重复，注释调一下程序
        # node = self.root
        # while node and node.data != search_data:  # node不为空且node的值不等于看，不断的循环
        #     if search_data < node.data:
        #         node = node.left
        #     else:
        #         node = node.right
        # return node
    '''
    查找，返回查找到的节点和它的父节点（内部接口）
    '''
    def _search(self, search_data):
        parent = None
        node = self.root
        while node and node.data != search_data:  # node不为空且node的值不等于看，不断的循环
            parent = node  # 如果查找到了，通过这个赋值，就保留了查找到的节点的父节点
            if search_data < node.data:
                node = node.left
            else:
                node = node.right
        return node, parent
    '''
    插入节点
    '''
    def insert(self, search_data):
        node, parent = self._search(search_data)
        if node:  # 如果返回的node不为空，则说明要插入的节点在树中已经存在
            return  # 什么都不返回

        node = TreeNode(search_data)  # 构造一个节点
        if parent is None:  # 如果整个树都是空的，
            self.root = node
        elif search_data < parent.data:  # 如果要插入的节点数据小于父节点数据
            parent.left = node  # 插入到左边
        else:
            parent.right = node  # 插入到右边

    '''
    删除节点
    '''
    def delete(self, search_data):
        pass


from collections import deque
# 层序遍历二叉树的各个节点
def levelOrder(root):
    q = deque([root])
    while q:
        node = q.popleft()  # 出队列
        print(node)

        if node.left:
            q.append(node.left)  # 入队左孩子
        if node.right:
            q.append(node.right)  # 入队右孩子


bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(37)
levelOrder(bst.root)
print(bst.search(98))   # 返回None
print(bst.search(10))   # 返回10
