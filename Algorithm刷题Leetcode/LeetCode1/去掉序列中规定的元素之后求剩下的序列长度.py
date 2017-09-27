# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 21:41'
"""
Remove Element

这个题目的意思是去掉序列中规定的元素之后求剩下的序列的长度，非常简单
"""

def removeElement(A, elem):
    """
    :param A:   a list of integers
    :param elem:  an integer, value need to be removed
    :return:  an integer
    """
    while elem in A:
        A.remove(elem)
        return len(A)
A = [1, 3, 4, 6]
print(removeElement(A, 3))  # 3