# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/25 10:51'

import inspect

# create a generation
def myGeneration():
    yield 1
    yield 2
    yield 'a'
print(inspect.isgeneratorfunction(myGeneration))  # 检测myGeneration是否是生成器
print(inspect.isgeneratorfunction(sum))  # 检测myGeneration是否是生成器

g = myGeneration()
for i in range(3):
   print(next(g))


