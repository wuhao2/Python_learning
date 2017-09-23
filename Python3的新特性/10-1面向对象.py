# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 16:47'
class C(object):
    def __init__(self, a):
        print('C', a)

class D(C):
    def __init(self, a):
        super().__init__(a)  # 调用父类C的构造函数

D(8)
