# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 20:32'

from lib1 import Circle
from lib2 import Rectangle
from lib3 import Triangle


# 由于在lib1、lib2、lib3中的获取面积的方法名字都不一样
def getArea(shape):
    for name in ('area', 'getArea', 'get_area'):
        f = getattr(shape, name, None)
        if f:
            return f()

shape1 = Circle(2)  # 12.56
shape2 = Triangle(3, 4, 5)  # 6.0
shape3 = Rectangle(6, 4)  # 24

shapes = [shape1, shape2, shape3]
print(list(map(getArea, shapes)))  # 得到面积为[12.56,  6.0,  24]


#############################################################
# 也可以利用标准库operator中的methodcaller实现
# from operator import methodcaller
# s = 'abc123abc456'
# s.find('abc', 4)
# methodcaller('find', 'abc', 4)
# methodcaller('find', 'abc', 4).s
