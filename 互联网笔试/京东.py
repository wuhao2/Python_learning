# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/8 13:55'

def func(x):
    count = 0
    while x:
        count += 1
        x &= x - 1
    return count
print(func(2015))

