
# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 10:06'

from random import randint, sample
# s = sample('abdefg', randint(3, 6))  # 随机产生一个列表，列表中元素为3-6个
# print(s)
d1 = {x: randint(1,4) for x in sample('abdefg', randint(3, 6))}
d2 = {x: randint(1,4) for x in sample('abdefg', randint(3, 6))}
d3 = {x: randint(1,4) for x in sample('abdefg', randint(3, 6))}
print(d1)
print(d2)
print(d3)
res = []
for k in d1:
    if k in d2 and k in d3:
        res.append(k)
print(res)  # 查找公共键


# 利用集合查找公共键
# set_data = d1.keys() & d2.keys() & d3.keys()  # 交集找公共键
# print(set_data)
from functools import reduce
# map reduce函数求n轮的交集
commom_data = reduce(lambda a, b: a & b, map(dict.keys, [d1, d2, d3]))
print(commom_data)


"""
  python中的reduce内建函数是一个二元操作函数，
  他用来将一个数据集合（链表，元组等）中的所有数据进行下列操作：
  用传给reduce中的函数 func()（必须是一个二元操作函数）先对集合中的第1，2个数据进行操作，
  得到的结果再与第三个数据用func()函数运算，最后得到一个结果。
"""
def myadd(x,y):
    return x+y
sum=reduce(myadd, (1, 2, 3, 4, 5, 6, 7))
print (sum)
"""
python map函数用法
很简单，第一个参数接收一个函数名，第二个参数接收一个可迭代对象
"""
def add(num):
    return num + 1
lt = [1, 2, 3, 4, 5, 6]
rs = map(add, lt)
print(rs)  # [2,3,4,5,6,7]