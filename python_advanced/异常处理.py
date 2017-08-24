# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/21 10:05'
"""
记录错误logging

如果不捕获错误，自然可以让Python解释器来打印出错误堆栈，
但程序也被结束了。既然我们能捕获错误，就可以把错误堆栈打印出来，
然后分析错误原因，同时，让程序继续执行下去。

Python内置的logging模块可以非常容易地记录错误信息：
"""

# err_logging.py
import logging
# def foo(s):
#     return 10 / int(s)
# def bar(s):
#     return foo(s) * 2
# def main():
#     try:
#         bar('0')
#     except Exception as e:
#         logging.exception(e)
#
# main()
# print('END')
# 调试方式一：
# 用print()最大的坏处是将来还得删掉它，想想程序里到处都是print()，
# 运行结果也会包含很多垃圾信息

# 调试方式2：
# assert的意思是，表达式n != 0应该是True，否则，
# 根据程序运行的逻辑，后面的代码肯定会出错。
# 如果断言失败，assert语句本身就会抛出AssertionError：
# 序中如果到处充斥着assert，和print()相比也好不到哪去。
# 不过，启动Python解释器时可以用-O参数来关闭assert

# import logging
# logging.basicConfig(level=logging.INFO)
# import logging
# s = '0'
# n = int(s)
# logging.info('n = %d' % n)
# print(10 / n)


# 第4种方式是启动Python的调试器pdb，
# 让程序以单步方式运行，可以随时查看运行状态。我们先准备好程序：
# python3 -m pdb err.py
# 任何时候都可以输入命令p 变量名 来查看变量，用命令c继续运行：
# 输入命令q结束调试，退出程序：
# err.py
import pdb
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)