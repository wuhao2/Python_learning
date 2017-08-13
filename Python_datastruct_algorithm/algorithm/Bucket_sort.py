# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/16 11:35'

#Python桶排序, 最快的排序方法
def bucket(lst):
    buckets = [0] * ((max(lst) - min(lst))+1)  # 创建一个列表

    for i in range(len(lst)):  # 标记
        buckets[lst[i]-min(lst)] += 1

    res = []
    for i in range(len(buckets)):   # 排序
        if buckets[i] != 0:
            res += [i+min(lst)]*buckets[i]
    return res

a = [12, 4, -2, 4, 56, -1, 4, 212]
b = bucket(a)
print(b)