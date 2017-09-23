# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 16:43'
import platform
print('Python', platform.python_version())

my_generator = (letter for letter in 'abcdefg')
next(my_generator)
# my_generator.next()  # python3中报错，不能调用函数
