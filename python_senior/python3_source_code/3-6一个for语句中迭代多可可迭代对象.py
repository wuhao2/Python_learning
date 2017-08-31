# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 16:22'

from random import randint
Chinese = [randint(60, 100) for _ in range(10)]
math = [randint(60, 100) for _ in range(10)]
English = [randint(60, 100) for _ in range(10)]
print('Chinese', Chinese)
print('math', math)
print('English', English)
total = []
for c, m, e in zip(Chinese, math, English):  # 在一个for语句中，并行迭代
    total.append(c + m + e)
print('total:', total)

##############################################################################
from itertools import chain  # 用链条连起来迭代
count = 0
for x in chain(Chinese, math, English):  # 在一个for语句中，串行迭代
    if x > 90:
        count += 1
print("count_nums: ", count)