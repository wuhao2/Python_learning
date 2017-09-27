# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/27 18:56'
"""
求X的平方根，如果不直接用x^2来计算的话，则采用牛顿法
"""
def sqrt(x):
    result = x/2.0
    while abs(result*result - x) > 0.00001:
        result = (result + x/result) / 2.0
    return(int(result))