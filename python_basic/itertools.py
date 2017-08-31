# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/25 14:05'

from itertools import chain
from itertools import combinations

test = chain('AB', 'CDE', 'F')
test1 = combinations([1, 2, 3, 4], 2)

for el in test1:
    print(el)
