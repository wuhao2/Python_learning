# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/20 15:51'

"""
from multiprocessing import Process
from multiprocessing import Queue, Pipe   # 多进程中使用管道与队列通信
q = Queue()  # 创建一个队列
q.put(1)  # 入队
print(q.get())  # 出队
def f(c):
    c.send(c.recv() * 2)
c1, c2 = Pipe()  # 创建2个管道
c1.send(55)
Process(target=f, args=(1,)).start()
print(c1.recv())

def f(s):
    print(s)
p = Process(target=f, args=('hello',))
p.start()

def f(q):
    print('start')
    print(q.get())
    print('end')
Process(target=f, args=(q,)).start()
q.put(1000)
"""





from threading import Thread
from multiprocessing import Process


def isArmStrong(n):  # 是否是水仙花数
    a, t = [], n
    while t > 0:
        a.append(t % 10)
        t /= 10
    k = len(a)
    return sum(x ** k for x in a) == n


def findArmStrong(a, b):
    print(a, b)
    res = [k for k in range(a, b) if isArmStrong(k)]
    print("%s - %s :%s" % (a, b, res))


def findByThread(*argslist):
    workers = []
    for args in argslist:
        worker = Thread(target=findArmStrong, args=args)  # 创建线程
        workers.append(worker)
        worker.start()   # 启动线程
    for t in workers:
        t.join()  # 等待线程执行完成


def findByProcess(*argslist):
    workers = []
    for args in argslist:
        worker = Process(target=findArmStrong, args=args)  # 创建进程
        workers.append(worker)
        worker.start()  # 启动进程
        for _ in workers:
            worker.join()   # 等待进程执行完毕

if __name__ == '__main__':
    import time
    start = time.time()
    # 传入两个tuple类型参数，即两个进程执行
    findByProcess((20000000, 25000000), (25000000, 30000000))
    # 传入两个参数，即两个线程执行
    # findByThread((20000000, 25000000), (25000000, 30000000))
    print(time.time() - start)

