# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 18:14'


# 如何派生内置不可变类型
class IntTuple(tuple):
    @staticmethod
    def __new__(cls, iterable):
        g = (x for x in iterable if isinstance(x, int) and x > 0)
        return super(IntTuple, cls).__new__(cls, g)

    @staticmethod
    def __int__(self, iterable):
        # before
        # print(self)
        super(IntTuple, self).__init__(iterable)


t = IntTuple([1, -1, 'abc', 6, ['x', 'y'], 3])
print(t)
# (1, -1, 'abc', 6, ['x', 'y'], 3)
# (1, 6, 3)  过滤之后，只存在正整数

