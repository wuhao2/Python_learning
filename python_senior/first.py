# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/25 13:32'

from first import first

first([0, False, None, [], (),42])
first([-1, 0, 1, 2])
first([-1, 0, 1, 2], key=lambda x: x>0)

