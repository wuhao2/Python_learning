# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/3 19:59'

import time
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(3)

# test three thread
def test_function(num1, num2):
    print(num1, num2)
    time.sleep(10)
    return num1 + num2
"""
使用三个线程，占用线程池全部线程 # 由于我们的结果是十秒后返回，所以这里也会被阻塞，十秒后才会收到结果
"""
t1 = datetime.now()
result_iterators = executor.map(test_function, [1, 2, 3], [5, 6, 7])  # map batch execute
for result in result_iterators:
    print(result)
"""
到这里很显然前面三个线程都在使用中，10秒后才能得到执行
"""

future = executor.submit(test_function, 4, 8)
t2 = datetime.now()
print(future.result())
print(t2 - t1)

