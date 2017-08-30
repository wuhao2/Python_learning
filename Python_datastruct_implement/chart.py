# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 15:40 '


# 有向图的实现
def path(chart, startNode, endNode, pathd=[]):  # 开始时路径为空
    pathd += [startNode]
    if startNode == endNode:  # 初始节点和终点重合
        return pathd

    if startNode not in chart:  # 如何没有上游节点，即字典中没有startNode这个键
        return None  # 返回没有路径

    for Node in chart[startNode]:
        if Node not in pathd:
            newNode = path(chart, Node, endNode, pathd)  # 递归调用
            if newNode:
                return newNode


chart = {"A": ["B", "D"], "C": ["E"], "D": ["C", "E"]}  # python中的字典可以描述图
print(path(chart, "A", "E"))

"""
图
        A
             B
D
                   C
    E
"""
