# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/19 14:36'

#
# def func(a):
#     '''func describtion'''
#     a = 2
#     return lambda k: a ** 2
# print(func.__doc__, " \n", func.__module__)
# g = func(10)
# print(g)
# c = g.__closure__[0]
# print(c.cell_contents)  # 访问闭包

#############################################################
"""
f.name 函数的名字
f.doc 函数文档字符串
f.module 函数所属模块名称
f.dict 函数的属性字典
f.defaults 默认参数元组
f.closure 函数闭包
"""
from functools import wraps, update_wrapper


def log(level="low"):
    def deco(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            ''' I am wrapper function'''
            print("log was in...")
            if level == "low":
                print("detailes was needed")
            return func(*args, **kwargs)
        # wrapper.__name__ = func.__name__
        # update_wrapper(wrapper, func, ('__name__', '__doc__'), ('__dict__',))
        return wrapper
    return deco


@log()
def myFunc():
    '''I am myFunc...'''
    print("myFunc was called")

print(myFunc.__name__)
myFunc()