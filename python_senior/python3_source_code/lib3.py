# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 20:40'
# lib3.py

class Triangle(object):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getArea(self):
        a, b, c = self.a, self.b, self.c
        p = (a + b + c) // 2
        area = (p* (p-a) * (p-b) * (p-c)) ** 0.5
        return area
