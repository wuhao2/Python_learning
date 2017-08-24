# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/20 15:12'
# 8-5 如何使用线程池
# 解决方案:
# 线程池是指分配固定个数的线程
# 线程池 python3
# 标准库中concurrentfutues下的ThreadPoolExecutor
# 对象的submit 和 map方法可以用来启动线程池中线程执行任务

from concurrent.futures import ThreadPoolExecutor
executor = ThreadPoolExecutor(3)  # 创建3个线程


def f(a, b):
    print('f', a, b)
    return a ** b

future = executor.submit(f, 2, 3)  # 执行一个线程
print("execute result: ", future.result())  # result（）会等到f（）执行完，才返回

print(executor.map(f, [2, 3, 4], [4, 5, 6]))  # 同时执行3个线程2^3, 3^5, 4^6
# 第一个线程执行 f 2 3
# 第二线程 执行f 3 5
# 第三个执行 f 4 6
# 当线程数超过线程池总数时，就会等待