# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/20 8:56'

import logging
from time import localtime, time, strftime, sleep


class CallingInfo(object):
    def __init__(self, name):
        log = logging.getLogger(name)
        log.setLevel(logging.INFO)
        fh = logging.FileHandler(name + '.log')  # 最终的log文件的文件名
        log.addHandler(fh)
        log.info("start...".center(50, '-'))  # log中的第一行
        self.log = log  # 实例属性
        self.formatter = '%(func)s -->[%(time)s -- %(used)s -- %(ncalls)s --]'  # 输出格式

    def info(self, func):
        def wrapper(*args, **kwargs):
            wrapper.ncalls += 1
            lt = localtime()
            start = time()
            res = func(*args, **kwargs)
            used = time() - start
            info = {}
            info['func'] = func.__name__
            info['time'] = strftime('%x %X', lt)  # 08/20/17 09:04:24
            info['used'] = used
            info['ncalls'] = wrapper.ncalls
            msg = self.formatter % info  # 用字典格式化输出信息为msg
            self.log.info(msg)
            return res
        wrapper.ncalls = 0  # 函数内的一个静态变量

        return wrapper

    def setFormater(self, formatter):
        self.formatter = formatter

    def turnOn(self):
        self.log.setLevel(logging.INFO)

    def turnOff(self):
        self.log.setLevel(logging.WARN)

cinfo1 = CallingInfo('../regular_file/mylog1')
cinfo2 = CallingInfo('../regular_file/mylog2')
cinfo1.setFormater('%(func)s --->[%(time)s -- %(used)s -- %(ncalls)s --]')
cinfo2.turnOn()

@cinfo1.info
def f():
    print("in f")

@cinfo1.info
def g():
    print('in g')

@cinfo2.info
def h():
    print('in h')

from random import choice
for _ in range(50):
    choice([f, g, h])()
    sleep(choice([0.5, 1, 1.5]))