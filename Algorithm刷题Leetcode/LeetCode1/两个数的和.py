# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 21:53'

"""
Two Sum

需找出一个列表中是否有两个数的和为一个给定的数，并返回这两个数的下标。
需要用到python里面的字典（相当于hash表），判断第i个数前面是否有一个数的值为target - num[i]
"""

"""这个貌似很高效啊"""
def twoSum(num, target):
    tmp = {}
    for i in range(len(num)):
        if target - num[i] in tmp:
            return tmp[target - num[i]] + 1, i + 1
        else:
            tmp[num[i]] = i


print(twoSum([2, 4, 6, 1], 7))
