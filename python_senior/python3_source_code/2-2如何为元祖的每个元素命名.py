# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/15 13:34'
"""
# 将索引命名，提高程序的可读性
# NAME = 0
# AGE = 1
# SEX = 2
# EMAIL = 3
NAME, AGE, SEX, EMAIL = range(4)  # 列表拆包赋值
# 元组
student = ('Jim', 16, 'mail', 'Jim8979@126.com')

print(student[NAME])
print(student[AGE])
print(student[SEX])
print(student[EMAIL])
"""

# 利用标准库中的namedtuple 代替tuple，元组存储小，访问速度快
from collections import namedtuple
student = namedtuple('student', ['name', 'age', 'sex', 'email'])
s = student('Jim', 16, 'mail', 'jim234@126.com')
print(s)
print(s.age)
print(s.name)
print(s.sex)
print(s.email)
print(isinstance(s, tuple))  #s是tuple的子类

