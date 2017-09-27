import threading
# 使用普通的全局变量，进行通信，可能导致数据污染
# 使用函数传参，与调用函数，调用开销太大

# ------所以---创建全局ThreadLocal对象: ---一个特殊的全局变量，不会因为不同线程的操作 被污染
local_school = threading.local()

def process_student():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name  # 不同线程都操作此code，相互独立，
    process_student()

t1 = threading.Thread(target= process_thread, args=('dongGe',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('老王',), name='Thread-B')
t1.start()
t2.start()

# Hello, dongGe (in Thread-A)
# Hello, 老王 (in Thread-B)