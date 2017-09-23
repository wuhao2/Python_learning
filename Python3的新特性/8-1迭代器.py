# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 16:25'
import platform
print('Python', platform.python_version())

print(range(3))  # 返回可迭代对象range(0, 3)
print(type(range(3)))
print(list(range(3)))  # [0, 1, 2]
