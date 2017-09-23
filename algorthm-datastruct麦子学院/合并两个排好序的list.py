# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/7 16:54'
"""
合并两个已经排好序的列表，得到的从大到小排列的新列表 O(m+n)
"""
def merge(a, b):
    res = []

    # while (len(a) != 0) | (len(b) != 0):
    while (a != []) | (b != []):
        if not a:  # 如果列表a为空
            res.append(b[-1])
            b.pop()
        elif not b:  # # 如果列表为空
            res.append(a[-1])
            a.pop()
        elif a[-1] > b[-1]:
            res.append(a[-1])
            a.pop()
        else:
            res.append(b[-1])
            b.pop()

    return res

a = [2, 3, 8]
b = [1, 5, 9]
print(merge(a, b))
