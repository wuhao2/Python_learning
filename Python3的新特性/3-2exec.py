# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 15:08'

"""python2中是正确的， python3中报错，a未定义"""
# def foo():
#    exec('a=4')  # python给函数中局部变量赋值
#    print(a)
# foo()

"""python3中"""
def foo():
    _locals = locals()  # 副本
    exec('a=4', globals(), _locals)
    a = _locals['a']
    print(a)

foo()  # 4
