# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/25 13:41'

from functools import partial
from first import first
import operator


def greater_than(number, min1=0):
    return number > min1

first([-1, 0, 1, 2], key=lambda x: x>0)  # 将以函数用一行代码表示
first([-1, 0, 1, 2], key=partial(greater_than, min1=42))  # 应用partial改进  lambda的一行函数式编程， 实现对greater_than的封装
first([-1, 0, 1, 2], key=partial(operator.le, 0))   # 操作符的使用
