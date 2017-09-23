# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 15:43'
import timeit, platform


def test_range():
    for i in range(100):
        pass


def test_xrange():
    for i in xrange(100):
        pass


if __name__ == '__main__':
    from timeit import Timer

    print('Python', platform.python_version())
    t1 = Timer("test_range()", "from __main__ import test_range")
    t2 = Timer("test_xrange()", "from __main__ import test_xrange")
    print('test_range', t1.timeit())  # Python3中range（）比 Python2中的xrange 的效率提高了
    # print ('test_xrange',t2.timeit())

print(list(range(10)))  # Python3中，range返回的是可迭代对象，需要用list函数转化为列表
