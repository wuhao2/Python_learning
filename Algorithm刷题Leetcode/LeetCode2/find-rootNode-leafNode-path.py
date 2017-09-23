# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/12 15:05'
"""
Path Sum

这个题的意思是一颗二叉树上是否存在一条从根节点到叶子节点的路径，其上所有节点之和等于一个指定的数。
方法就是当我们从根节点往下递归时，看当前节点是否存在sum减去前面节点之和的路径存在。代码如下：
"""
def hasPathSum(root, sum):
    """
    :param root: a tree node
    :param sum: a integer
    :return: bool
    """
    result = False
    if root is None:
        return result
    else:
        sum -= root.val  # 从根节点出发
        if sum == 0 and root.left is None and root.right is None:
            result = True
            return result
        else:
            if root.left:
                result = result or hasPathSum(root.left, sum)
            if root.root:
                result = result or hasPathSum(root.right, sum)
            return result