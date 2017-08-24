# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 20:40'
# lib2.py


class Rectangle(object):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def get_area(self):
        return self.w * self.h

