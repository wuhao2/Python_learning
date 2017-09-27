from threading import Thread, Lock
from time import sleep

# 如果不加锁，这三个线程的执行竞争关系，这是由os决定的
# 加了三把锁之后，能够保证三个线程的有序执行-----即线程同步
class Task1(Thread):
    def run(self):
        while True:
            if lock1.acquire():  # 1上锁
                print("------Task 1 -----")
                sleep(0.5)
                lock2.release()  # 2解锁


class Task2(Thread):
    def run(self):
        while True:
            if lock2.acquire():  # 2上锁
                print("------Task 2 -----")
                sleep(0.5)
                lock3.release()  # 3解锁


class Task3(Thread):
    def run(self):
        while True:
            if lock3.acquire():  # 3上锁
                print("------Task 3 -----")
                sleep(0.5)
                lock1.release()  # 1解锁


# 使用Lock创建出的锁默认没有“锁上”
lock1 = Lock()

# 创建另外一把锁，并且“锁上”
lock2 = Lock()
lock2.acquire()

# 创建另外一把锁，并且“锁上”
lock3 = Lock()
lock3.acquire()

t1 = Task1()
t2 = Task2()
t3 = Task3()

t1.start()
t2.start()
t3.start()
