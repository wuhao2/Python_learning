# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 14:32'

# 使用生成器函数实现可迭代对象
def f():
    print('in f(), 1')
    yield 1
    print('in f(), 2')
    yield 2
    print('in f(), 3')
    yield 3
    raise StopIteration

# g = f()  # 实例化生成器对象，即实现了可迭代接口__iter__，也实现了迭代器接口__next__
# print(g.__iter__() is g)  # return True , g is iterable object
# for x in g:
#     print(x)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# 找素数
class PrimeNumbers:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def isPrimeNum(self, k):
        if k < 2:
            return False
        for i in range(2, k):
            if k % 2 == 0:
                return False
        return True

    def __iter__(self):  # 将__iter__实现成生成器函数
        for k in range(self.start, self.end+1):
            if self.isPrimeNum(k):
                yield k

# 测试
for x in PrimeNumbers(1, 100):
    print(x, ' ', end='')
