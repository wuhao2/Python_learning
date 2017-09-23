# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 15:56'
"""
找到一个数组的peak element(该元素比起邻居都大的元素)，很简单，
需要注意的是这个题只需要返回一个值即可
"""
def findPeakElement(num):
    i = 0
    while i < len(num):
        if i == 0 and (len(num) == 1 or num[i] > num[i+1]):  # 第一个数
            return i
        if i == len(num) - 1 and (len(num) == 1 or num[i] > num[i-1]):  # 最后一个数
            return i
        if num[i] > num[i-1] and num[i] > num[i+1]:  # 大于左边，同时大于右边
            return num[i]
        i += 1
l = [9, 2, 7, 8, 4, 3, 5]
print(findPeakElement(l))