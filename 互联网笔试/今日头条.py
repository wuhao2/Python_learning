# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/10 19:34'

from random import randint
from random import choice, sample

def inputOutput(n, k):
    userFavoritDegree = [randint(0, n) for _ in range(n)]
    print(len(userFavoritDegree))
    print(userFavoritDegree)

    index = [range(len(userFavoritDegree))]  # 下标

    while True:
        q = [sample(index, 2) for i in range()]
        print(len(q))

        for i in range(0, len(userFavoritDegree)):
            if i % 3 == 0:
                if userFavoritDegree[index] == k:
                    print("l, r, k", index, end='')
