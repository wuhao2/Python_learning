# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 19:13'
from math import pi


class Circle(object):
    def __init__(self, radius):
        self.radius = radius

    def getRadius(self):
        return self.radius

    def setRadius(self, value):
        if not isinstance(value, (int, float)):
            raise ValueError('wrong type.')
        self.radius = float(value)

    def getArea(self):
        return self.radius ** 2 * pi
    # @property
    # 内置的属性创建可管理的属性
    R = property(getRadius, setRadius)

c = Circle(3.2)
print(c.getArea())

# c.radius = 'afg'
# print(c.getRadius())  # afg没有报错，所以应该设置可管理的属性

c.R = 'avdf'
print(c.R)   # ValueError: wrong type.

