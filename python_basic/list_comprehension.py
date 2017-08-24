# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/25 11:12'

x = [word.capitalize()
        for line in ("hello world?", "world!", "or not")
        for word in line.split()
        if not word.startswith('or')]
print(x)
