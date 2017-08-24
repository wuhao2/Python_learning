# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 19:26'
from functools import total_ordering
from abc import ABCMeta, abstractmethod


@total_ordering  # 装饰器
class Shape(object):

    @abstractmethod
    def area(self):
        pass

    def __lt__(self, other):
        print('in __lt__')
        if isinstance(other, Shape):
            raise TypeError('other is not shape')
        return self.area() < other.area()

    def __le__(self, other):
        print('in __le__')
        if isinstance(other, Shape):
            raise TypeError('other is not shape')
        return self.area() <= other.area()

    def __eq__(self, other):
        print('in __eq__')
        if isinstance(other, Shape):
            raise TypeError('other is not shape')
        return self.area() == other.area()


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14


r1 = Rectangle(7, 3)
r2 = Rectangle(5, 3)
c1 = Circle(3)

print(r1 <= r2)
print(c1 <= r2)
