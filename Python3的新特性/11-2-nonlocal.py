# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 18:06'


def out_function():
    call_count = 0

    def in_function():
        nonlocal call_count  # 内层函数调用外层变量时使用
        call_count += 1
        print('call_count', call_count)

    return in_function


out_function()()
