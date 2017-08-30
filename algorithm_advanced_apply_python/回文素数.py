# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 16:52 '
"""
问题描述:
所谓回文素数是指，对一个整数n从左向右和从右向左读结果值相同且是素数，
即称为回文素数。

求不超过1000的回文素数。
"""

import math


def isPrimeNumber(n):  # 优化，上面的函数每次要遍历一遍，效率不高
    for i in range(2, int(math.sqrt(n) + 1)):
        # 其实只需要让n除以 2到int(math.sqrt(n) + 1)，不需要要除以 2到n，效率提高了
        if n % i == 0:
            return False
        else:
            return True


def Reverse(num):
    rNum = 0
    while num:
        rNum = rNum * + num % 10
        num = int(num / 10)
    return rNum


def RPrimeNumber(num):
    arr = []
    i = 2
    while i < num:
        if isPrimeNumber(i) and i == Reverse(i):
            arr.append(i)
        i += 1
    return arr


print(RPrimeNumber(1000))
