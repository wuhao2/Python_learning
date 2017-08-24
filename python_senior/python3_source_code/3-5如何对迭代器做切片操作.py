# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 16:04'
# 如何对一个迭代器进行切片操作
from itertools import islice

file = open('word.txt', 'rb')

# 这种读取方式虽然可行，，但是一般日志文件大小都是几个G，一次性读取是个灾难
# lines = file.readlines()
# print(lines)
# print()

#采用的islice是可迭代的
for line in islice(file, 0, 5):  # 迭代前5行
    print(line)
