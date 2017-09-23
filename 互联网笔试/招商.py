# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/13 20:01'

a, b, n = input("please input:").split(' ')
print(a, b, n)
print(type(a), type(b), type(n))

def CommonMutipleCount(a, b, n):
    res = []
    s = a * b
    i = 1
    while (i*s) <= n:
        i += 1
        res.append(i*s)
    return len(res)
print(CommonMutipleCount(int(a), int(b), int(n)))