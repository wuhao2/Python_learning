# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 20:40'
# lib1.py


class Circle(object):
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * 3.14
