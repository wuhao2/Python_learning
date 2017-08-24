# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/21 15:01'
'''
import os
print('Process (%s) start...' % os.getpid())
# Only works on Unix/Linux/Mac:
pid = os.fork()
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))
'''

# 由于Windows没有fork调用，上面的代码在Windows上无法运行。由于Mac系统是基于BSD（Unix的一种）内核，
# 所以，在Mac下运行是没有问题的，推荐大家用Mac学Python！
# 有了fork调用，一个进程在接到新任务时就可以复制出一个子进程来处理新任务，
# 常见的Apache服务器就是由父进程监听端口，每当有新的http请求时，就fork出子进程来处理新的http请求。
# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__ == '__main__':
#     print('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print('Child process will start.')
#     p.start()
#     p.join()
#     print('Child process end.')
'''
Pool
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
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

'''
# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。
# import subprocess
# print('$ nslookup www.python.org')
# r = subprocess.call(['nslookup', 'www.python.org'])
# print('Exit code:', r)


# import subprocess
# print('$ nslookup')
# p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE,
#                      stdout=subprocess.PIPE, stderr=subprocess.PIPE)
# output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
# print('Exit code:', p.returncode)
'''
进程间通信

Process之间肯定是需要通信的，操作系统提供了很多机制来实现进程间的通信。
Python的multiprocessing模块包装了底层的机制，提供了Queue、Pipes等多种方式来交换数据。
我们以Queue为例，在父进程中创建两个子进程，一个往Queue里写数据，一个从Queue里读数据
'''
# from multiprocessing import Process, Queue
# import os, time, random
#
# # 写数据进程执行的代码:
# def write(q):
#     print('Process to write: %s' % os.getpid())
#     for value in ['A', 'B', 'C']:
#         print('Put %s to queue...' % value)
#         q.put(value)
#         time.sleep(random.random())
#
# # 读数据进程执行的代码:
# def read(q):
#     print('Process to read: %s' % os.getpid())
#     while True:
#         value = q.get(True)
#         print('Get %s from queue.' % value)
#
# if __name__ == '__main__':
#     # 父进程创建Queue，并传给各个子进程：
#     q = Queue()
#     pw = Process(target=write, args=(q,))
#     pr = Process(target=read, args=(q,))
#     # 启动子进程pw，写入:
#     pw.start()
#     # 启动子进程pr，读取:
#     pr.start()
#
#     pw.join()  # 等待pw结束:
#     # pr进程里是死循环，无法等待其结束，只能强行终止:
#     pr.terminate()

# 结果：
# Process to write: 12228
# Put A to queue...
# Process to read: 14768
# Get A from queue.
# Put B to queue...
# Get B from queue.
# Put C to queue...
# Get C from queue.
"""
小结

在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。
"""
##########################################################################################
import time, threading

# 新线程执行的代码:
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


# if __name__ == '__main__':
#     print('thread %s is running...' % threading.current_thread().name)
#     t = threading.Thread(target=loop, name='LoopThread')  # 创建一个线程，名为LoopThread
#     t.start()
#     t.join()
#     print('thread %s ended.' % threading.current_thread().name)

'''
Lock

多线程和多进程最大的不同在于，多进程中，同一个变量，各自有一份拷贝存在于每个进程中，
互不影响，而多线程中，所有变量都由所有线程共享，所以，任何一个变量都可以被任何一个线程修改，
因此，线程之间共享数据最大的危险在于多个线程同时改一个变量，把内容给改乱了。
'''
import time, threading

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()   # 定义全局解释锁
def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        # 先要获取锁:
        lock.acquire()
        try:
            # 放心地改吧:
            change_it(n)
        finally:
            # 改完了一定要释放锁:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''
如果我们要确保balance计算正确，就要给change_it()上一把锁，
当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，
因此其他线程不能同时执行change_it()，只能等待，直到锁被释放后，
获得该锁以后才能改。由于锁GIL只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，
所以，不会造成修改的冲突。创建一个锁就是通过threading.Lock()来实现：
'''


# 试试用Python写个死循环：
# import threading, multiprocessing
#
# def loop():
#     x = 0
#     while True:
#         x = x ^ 1
#
# for i in range(multiprocessing.cpu_count()):
#     t = threading.Thread(target=loop)
#     t.start()
'''
启动与CPU核心数量相同的N个线程，在4核CPU上可以监控到CPU占用率仅有102%，也就是仅使用了一核。

但是用C、C++或Java来改写相同的死循环，直接可以把全部核心跑满，
4核就跑到400%，8核就跑到800%，为什么Python不行呢？

因为Python的线程虽然是真正的线程，但解释器执行代码时，有一个GIL锁：Global Interpreter Lock，
任何Python线程执行前，必须先获得GIL锁，然后，每执行100条字节码，
解释器就自动释放GIL锁，让别的线程有机会执行。
这个GIL全局锁实际上把所有线程的执行代码都给上了锁，
所以，多线程在Python中只能交替执行，即使100个线程跑在100核CPU上，也只能用到1个核。

GIL是Python解释器设计的历史遗留问题，通常我们用的解释器是官方实现的CPython，
要真正利用多核，除非重写一个不带GIL的解释器。----PyPy解释器

Python虽然不能利用多线程实现多核任务，但可以通过多进程实现多核任务。
多个Python进程有各自独立的GIL锁，互不影响
'''

'''
# ThreadLocal应运而生
#  在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，
# 因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦
'''
import threading

# 创建全局ThreadLocal对象:
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student()

t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()

# 全局变量local_school就是一个ThreadLocal对象，每个Thread对它都可以读写student属性，
# 但互不影响。你可以把local_school看成全局变量，
# 但每个属性如local_school.student都是线程的局部变量，
# 可以任意读写而互不干扰，也不用管理锁的问题，ThreadLocal内部会处理。

# ThreadLocal最常用的地方就是为每个线程绑定一个数据库连接，HTTP请求，用户身份信息等，
# 这样一个线程的所有调用到的处理函数都可以非常方便地访问这些资


'''
如果用多进程实现Master-Worker，主进程就是Master，其他进程就是Worker。

如果用多线程实现Master-Worker，主线程就是Master，其他线程就是Worker。


多进程模式最大的优点就是稳定性高，因为一个子进程崩溃了，不会影响主进程和其他子进程。
（当然主进程挂了所有进程就全挂了，但是Master进程只负责分配任务，挂掉的概率低）
著名的Apache最早就是采用多进程模式。



多进程模式的缺点
是创建进程的代价大，在Unix/Linux系统下，用fork调用还行，
在Windows下创建进程开销巨大。另外，操作系统能同时运行的进程数也是有限的，
在内存和CPU的限制下，如果有几千个进程同时运行，操作系统连调度都会成问题。


多线程模式致命的缺点
就是任何一个线程挂掉都可能直接造成整个进程崩溃，因为所有线程共享进程的内存
多线程模式通常比多进程快一点，但是也快不到哪去,在Windows下，多线程的效率比多进程要高，
所以微软的IIS服务器默认采用多线程模式。
'''

"""
操作系统在切换进程或者线程时也是一样的:
它需要先保存当前执行的现场环境（CPU寄存器状态、内存页等），
然后，把新任务的执行环境准备好（恢复上次的寄存器状态，切换内存页等），才能开始执行。
这个切换过程虽然很快，但是也需要耗费时间。如果有几千个任务同时进行，
操作系统可能就主要忙着切换任务，根本没有多少时间去执行任务了，
这种情况最常见的就是硬盘狂响，点窗口无反应，系统处于假死状态。
"""

'''
(cpu)计算密集型 vs. IO密集型

第一种任务：计算密集型任务，比如计算圆周率、对视频进行高清解码等等由于主要消耗CPU资源，
因此，代码运行效率至关重要。Python这样的脚本语言运行效率很低，
完全不适合计算密集型任务。对于计算密集型任务，最好用C语言编写。

第二种任务：IO密集型，涉及到网络、磁盘IO的任务都是IO密集型任务，
这类任务的特点是CPU消耗很少，任务的大部分时间都在等待IO操作完成
（因为IO的速度远远低于CPU和内存的速度）。对于IO密集型任务，任务越多，CPU效率越高，
但也有一个限度。常见的大部分任务都是IO密集型任务，比如Web应用。
'''

"""
异步IO

现代操作系统对IO操作已经做了巨大的改进，最大的特点就是支持异步IO。
如果充分利用操作系统提供的异步IO支持，就可以用单进程单线程模型来执行多任务，
这种全新的模型称为事件驱动模型，Nginx就是支持异步IO的Web服务器，
它在单核CPU上采用单进程模型就可以高效地支持多任务。
在多核CPU上，可以运行多个进程（数量与CPU核心数相同），充分利用多核CPU。
由于系统总的进程数量十分有限，因此操作系统调度非常高效。
用异步IO编程模型来实现多任务是一个主要的趋势。
"""