# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 15:27'

"""
给定一个数组，判断从首位置能否到达最后一个位置。这个问题我们可以反过来看，
如果从第n-1个位置能够到达第n个位置，那么我们就可以判断前面n-2个位置能否到达第n-1个位置，
以此类推，如果最后能反推到第一个位置则说明可以，否则不行
"""
def canJump(A):
    index = len(A) - 1
    for i in reversed(range(len(A)-1)):  # 反向迭代
        if i + A[i] >= index:
            index = i
    return not index

A = [1, 3, 7, 9, 10]
print(canJump(A))