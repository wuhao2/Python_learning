# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 12:12'
"""
迭代器

迭代是Python最强大的功能之一，是访问集合元素的一种方式。。
迭代器是一个可以记住遍历的位置的对象。
迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
迭代器有两个基本的方法：iter() 和 next()。
字符串，列表或元组对象都可用于创建迭代器

"""
# import sys
# list1 = [1, 2, 3, 4]
# it = iter(list1)  # 创建迭代器对象
#
# for x in it:  # 迭代器对象可以使用常规for语句进行遍历
#     print(x, end=" ")
#
# while True:  # 也可以使用 next() 函数进行遍历
#     try:
#         print(next(it))  # 输出迭代器的下一个元素
#     except StopIteration:
#         sys.exit()


"""
生成器

在 Python 中，使用了 yield 的函数被称为生成器（generator）。
跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回yield的值。
并在下一次执行 next()方法时从当前位置继续运行。
以下实例使用 yield 实现斐波那契数列：

"""
import sys
# def fibonacci(n):  # 生成器函数 - 斐波那契
#     a, b, counter = 0, 1, 0
#     while True:
#         if (counter > n):
#             return
#         yield a
#         a, b = b, a + b
#         counter += 1
# f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
# while True:
#     try:
#         print(next(f), end=" ")
#     except StopIteration:
#         sys.exit()
##############################################################################################

# # 此函数
# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n += 1
# fab(10)
# # 结果没有问题，但有经验的开发者会指出，
# # 直接在 fab 函数中用 print 打印数字会导致该函数可复用性较差，
# # 因为 fab 函数返回 None，其他函数无法获得该函数生成的数列


# def fab(max):
#     n, a, b = 0, 0, 1
#     L = []
#     while n < max:
#         L.append(b)
#         a, b = b, a + b
#         n += 1
#     return L
# for n in fab(5):
#     print(n)
# # 改写后的 fab 函数通过返回 List 能满足复用性的要求，
# # 但是更有经验的开发者会指出，该函数在运行中占用的内存会随着参数 max 的增大而增大，
# # 如果要控制内存占用，最好不要用 List来保存中间结果，而是通过 iterable 对象来迭代。


class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    # def next(self):  # 在python3中应该使用__next__
    def __next__(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n += 1
            return r
        raise StopIteration()

for n in Fab(5):
    print(n)
# Fab 类通过 next() 不断返回数列的下一个数，内存占用始终为常数
# 然而，使用 class 改写的这个版本，代码远远没有第一版的 fab 函数来得简洁


# def fab(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b      # 使用 yield
#         # print b
#         a, b = b, a + b
#         n = n + 1
#
# for n in fab(5):
#     print(n)
# 第四个版本的 fab 和第一版相比，仅仅把 print b 改为了 yield b，
# 就在保持简洁性的同时获得了 iterable 的效果。
# 调用第四版的 fab 和第二版的 fab 完全一致
