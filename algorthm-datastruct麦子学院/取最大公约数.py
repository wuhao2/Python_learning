# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/7 20:32'

def gcd_mod(m, n):
    if n == 0:
        return m
    else:
        return gcd_mod(n, m % n)
print(gcd_mod(7, 3))

