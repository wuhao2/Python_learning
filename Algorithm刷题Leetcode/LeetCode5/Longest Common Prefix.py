# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 16:04'
"""
寻找字符数组中最长的共同前缀，找到最短的数组，然后每次加一个看是不是他们的前缀，
如果数组中含有一个‘’的话，则前缀为‘’。
"""
def longestCommonPrefix(strs):
    if len(strs) == 0:
        return('')
    if len(strs) == 1:
        return strs[0]
    idx = 0
    for i in range(1, len(strs)):
        if len(strs[i]) < len(strs[idx]):
            idx = i
    if len(strs[idx]) == 0:
        return ''
    tmp = ''
    for i in range(len(strs[idx])):
        tmp1 = tmp + strs[idx][i]
        for j in range(len(strs)):
            if strs[j].find(tmp1) != 0:
                return tmp
        tmp = tmp1
        if i == len(strs[idx]) - 1:
            return tmp