# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/13 10:54'
# Kruskal算法python实现
# 一、问题描述
#
# 读入distance.txt中的点阵，数值表示两点间的欧氏距离，利用Kruskal算法建立一棵最小生成树。
#
# 二、思路分析
#
# 可以利用并查集这一数据结构来描述这个过程。按照wikipedia上的解释，并查集是一种树型的数据结构，常用于处理一些不相交集合的合并及查询问题，其上定义两种操作 find 和 union 。在kruskal算法中，只需要将edges排好序后，再判断他们的root相不相同，不相同则union二者并把这个edge填入树中即可。
#
# 三、具体实现
#
# 基本数据类型设定
#
# 图使用包含vertice和edge的字典


# vertice 的两个属性
# Parent[vertice] 代表其父节点，在find函数中父节点指向根节点
# Rank[vertice] 代表节点的秩，秩越高，则离根节点越近
# 并查集实现
# makeset函数，用于初始化vertice

graph = {
    'vertices':[],
    'edges': set()
}
def makeset(vertice):
    Parent[vertice] = vertice
    Rank[vertice] = 0

# find函数，用于找到根节点
def find(vertice):
    Parent[vertice]=(Parent[vertice]==vertice and vertices or find(vertices ))
    return Parent[vertice]

# union函数，用于联通两个子块
def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if Rank[root1] > Rank[root2]:
            Parent[root2] = root1
        else:
            Parent[root1] = root2
            if Rank[root1] == Rank[root2]:
                Rank[root2] += 1

# kruskal函数
def kruskal(graph):
    for vertice in graph['vertices']: makeset(vertice)
    minimum_spanning_tree = set()
    edges = [i for i in graph['edges']]
    edges.sort()
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree