# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 13:13'

def searchInsert(list, target):
    for i in range(len(list)):
        if list[i] >= target:
            return i
        if list[len(list) - 1] < target:
            return len(list)
l = [1, 2, 3, 4, 6]  # 已经排好序了
print(searchInsert(l, 4))