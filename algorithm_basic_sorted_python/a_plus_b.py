# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/26 15:48'

def aplusb(a, b):
    wuhao = 1
    while wuhao != 0:
        s = a ^ b
        wuhao = (a & b) << 1
        a = s
        b = wuhao
    return a
print(aplusb(3, 2))
