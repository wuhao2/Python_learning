# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 16:10'
"""
给定整数n和k，输出长度为k的有1到n的组合有多少个。思路是比如说对于k=2到k=3,
我们其实相当于在k的基础上加上比第二大但是不大于n的这么多种组合方式，所以可以利用迭代。
"""
def combine(n, k):
    result = []
    if k == 1:
        for i in range(1, n + 1):
            result.append([i])
        return result
    result = combine(n, k-1)
    tmp = []
    for res in result:
        for i in range(res[-1] + 1, n + 1):
            tmp.append(res + [i])
    return tmp
print(combine(3, 5))