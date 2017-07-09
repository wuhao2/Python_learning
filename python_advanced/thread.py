# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/3 19:59'
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(10)


def test_function(num1, num2):
    print(num1, num2)
    return num1 + num2

future = executor.submit(test_function, 1, 2)  # submit execute
print(future.result())

result_iterators = executor.map(test_function, [1, 2], [5, 5])  # map batch execute
for result in result_iterators:
    print(result)

""" executor.map(function, 参数1_list, 参数2_list, 参数n_list)
参数1_list: 代表方法第一个参数的列表
参数2_list: 代表方法第二个参数的列表
如： executor.map(test_function, [1, 2], [5, 5]) 代表，执行test_function方法，
第一个线程的参数为1和5，
第二个线程的参数为2和5。
线程1：test_function(1, 5) 结果为1 + 5 = 6 该方法返回的是一个可迭代的对象，
里面直接包含了每个方法执行的结果，不需要调用result()方法。
"""
