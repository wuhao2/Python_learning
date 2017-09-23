# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 16:10'

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