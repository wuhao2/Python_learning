# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/20 16:31'
"""
计算1000个随机数的和，计算8次，利用8个线程执行
"""
# import random
# import threading
# import time
#
# result = []
# def compute():
#     result.append(sum([random.randint(1, 100) for _ in range(1000000)]))
# start_time = time.time()
# workers = [threading.Thread(target=compute) for x in range(8)]  # 创建8个线程
# for worker in workers:
#     worker.start()
# for worker in workers:
#     worker.join()
# used_time = time.time() - start_time
# print("result: %s" % result)
# print("used time: ", used_time)
# result: [50513335, 50450410, 50478401, 50493834, 50499918, 50539380, 50522753, 50473324]
# used time:  12.12531065940857
"""
计算1000个随机数的和，计算8次，利用8个进程执行
"""
# import multiprocessing
# import random
#
# def compute():
#     return sum([random.randint(1, 100) for _ in range(1000000)])
#
# pool = multiprocessing.Pool(8)
# print("results: %s" % pool.map(compute, range(8)))  # 启动8个进程执行
# pool.close()


from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')