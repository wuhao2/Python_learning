# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/19 15:18'
from functools import wraps

import time
import logging


def warn(timeout):
    # 将timeout实现为一个列表，就不需要使用python3中的nonlocal关键字了
    timeout = [timeout]

    def decorator(func):  # 生产装饰器的工厂
        def wrapper(*args, **kargs):
            start = time.time()
            res = func(*args, **kargs)
            used = time.time() - start
            if used > timeout[0]:
                msg = '"%s": %s > %s' % (func.__name__, used, timeout[0])
                logging.warning(msg)
            return res

        def set_timeout(k):
            # nonlocal timeout  # python3中的关键字
            timeout[0] = k

        wrapper.set_timeout = set_timeout
        return wrapper
    return decorator


from  random import randint


@warn(1.5)   # 带参数装饰器
def test():
    print('in test')
    while randint(0, 1):
        time.sleep(0.5)

for _ in range(30):  # 执行30次函数
    test()

# 修改了timeout
test.set_timeout(1)
for _ in range(30):  # 执行30次函数
    test()