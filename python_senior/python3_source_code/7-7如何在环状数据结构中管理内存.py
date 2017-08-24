# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 20:15'
# class A(object):
#     def __del__(self):
#         print("in A.__del__")
#
# a = A()
# b = a
# import sys
# count = sys.getrefcount(a)
# print(count)  # 3

import weakref  # 弱引用， 消除循环引用问题


# 循环引用的内存管理问题
class Data(object):
    def __init__(self, value, owner):
        self.owner = weakref.ref(owner)  # 解决循环引用
        self.value = value

    def __str__(self):
        return "%s's data, value is %s" % (self.owner(), self.value)

    def __del__(self):
        print('in Data.__del__')


class Node(object):
    def __init__(self, value):
        self.data = Data(value, self)

    def __del__(self):
        print('in Node.__del__')

node = Node(100)
del node
# raw_input('wait...')
