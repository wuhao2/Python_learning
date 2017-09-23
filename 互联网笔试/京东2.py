# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/8 19:59'

def func(n):
    res = []
    for i in range(1, n):
        if i:
            l = [i for _ in range(1, n+1)]
            res.extend(l)


if __name__ == "__main__":
    print(func(3))