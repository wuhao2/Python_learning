# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 12:29 '
# 找出100以内的勾股数
# a2 + b2 = c2 (a<b)
from time import time
import math
start = time()
for a in range(1, 10):  # a的范围[0,9]
    for b in range(a+1, 100):  # b[>a, 99]
        c = math.sqrt(a*a + b*b)  # 求平方根
        if c.is_integer():  # 判断是否是整数
            print(a, b, c)
end = time()
print("used time:", end-start)


