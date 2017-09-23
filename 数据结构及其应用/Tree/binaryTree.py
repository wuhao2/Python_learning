# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/19 10:28'


class Node(object):
    """节点类"""

    def __init__(self, elem=-1, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild


class Tree(object):
    """树类"""

    def __init__(self, root=None):
        self.root = root

    def add(self, item):
        node = Node(item)
        if self.root is None:  # 特殊情况，如果是空树
            self.root = node
        queue = [self.root]
        while queue:  # 利用广度优先添加，添加成一颗完全二叉树
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)
            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadthTravel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, root):
        """递归实现先序遍历"""
        if root is None:
            return
        print(root.elem)
        self.preorder(root.lchild)
        self.preorder(root.rchild)

    def inorder(self, root):
        """递归实现中序遍历"""
        if root is None:
            return
        self.inorder(root.lchild)
        print(root.elem)
        self.inorder(root.rchild)

    def postorder(self, root):
        """递归实现后续遍历"""
        if root is None:
            return
        self.postorder(root.lchild)
        self.postorder(root.rchild)
        print(root.elem)


if __name__ == "__main__":
    tree = Tree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    print(tree.breadthTravel())
