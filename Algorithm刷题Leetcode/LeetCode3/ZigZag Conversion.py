# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 10:21'
"""
字符串的映射，排列的形状就是由以前的一行变为类似于多个倒着的N这种形状的转换。
1. 如果是第一行或者最后一行，那么从第一个数开始到下一个数每次相差（2 * nRows - 2）
2. 对于其他行，这一行的数字的排列是奇数列和偶数列交替的，当然列号不一定是连续的，
   但是他们的列号肯定是奇偶交替的
3. 对于奇数列，两个“相邻”的之间相差2 * (nRows - 1 - i)这么多个数
4. 对于偶数列，两个“相邻”的之间相差2 * (nRows - i)这么多个数
"""


def convert(s, nRows):
    result = ''
    if s == '' or nRows <= 1:
        return s
    i = 0
    while i < len(s) and i < nRows:
        j = i
        result += s[j]
        k = 0
        while j < len(s):
            # 如果是第一行或最后一行
            if i == 0 or i == nRows - 1:
                j += 2 * nRows - 2
            else:
                if k == 0:  # 如果是奇数列
                    j += 2 * (nRows - 1 - i)
                    k = 1
                else:  # 如果是偶数列
                    j += 2 * i
                    k = 0
            # 不能超过字符串的长度
            if j < len(s):
                result += s[j]
        i += 1
    return result
