# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 15:39'
import platform
print('Python', platform.python_version())
i = 1
print('before: i =', i)
print('comprehension:', [i for i in range(5)])
print('after: i =', i)

# Python 3.5.3
# before: i = 1
# comprehension: [0, 1, 2, 3, 4]
# after: i = 1
"""在python2中,after: i = 4"""