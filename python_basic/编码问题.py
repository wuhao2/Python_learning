# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/20 17:34'

# 获取用户输入十进制数
dec = int(input("输入数字："))

print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))

# 搞清楚了ASCII、Unicode和UTF-8的关系，
# 我们就可以总结一下现在计算机系统通用的字符编码工作方式：
# 在计算机内存中，统一使用Unicode编码，当需要保存到硬盘或者需要传输的时候，
# 就转换为UTF-8编码。
# 用记事本编辑的时候，从文件读取的UTF-8字符被转换为Unicode字符到内存里，
# 编辑完成后，保存的时候再把Unicode转换为UTF-8保存到文件：
"""
在最新的Python 3版本中，字符串是以Unicode编码的，
也就是说，Python的字符串支持多语言：
"""
str = "吴浩"
print(str)
# Python提供了ord()函数获取字符的整数表示，
print(ord("A"))  # 65
print(ord("a"))  # 97
print(ord("0"))  # 48
# chr()函数把编码转换为对应的字符：
print(chr(48))
print(chr(65))
print(chr(97))
# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes
print('ABC'.encode('ascii'))  # b'ABC'
print(b'ABC'.decode('ascii'))  # ABC
print('中文'.encode('utf-8'))    # b'\xe4\xb8\xad\xe6\x96\x87'
print( b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文
# 1个中文字符经过UTF-8编码后通常会占用3个字节，而1个英文字符只占用1个字节
print(len(b'ABC'),len(b'\xe4\xb8\xad\xe6\x96\x87'),len('中文'.encode('utf-8')))  # 3 6 6


# 这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。
# 不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = "Y"
print('tuple：', t)
# 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，
# 而是list的元素。tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，
# 就不能改成指向其他对象，但指向的这个list本身是可变的！

# s = int(input('birth: '))  # 返回的是string,必须强转成int
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')


s1 = set([1, 2, 3])
s2 = set([4, 2, 3])
print(s1 & s2)  # {2, 3}


# a, b = b, a + b
# t = (b, a + b) # t是一个tuple
# a = t[0]
# b = t[1]



def power(x, n):  # 位置参数
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s
print(power(3, 3))  # 27


def power(x, n=2):  # 默认参数
    s = 1
    while n > 0:
        n -= 1
        s = s * x
    return s
print(power(3))  #9

def calc(numbers):  # 传入一个list
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 2, 3]))  # 14 计算a2 + b2 + c2 + ……

def calc(*numbers):  # 传入一个list
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))  # 14 计算a2 + b2 + c2 + ……

"""
关键字参数

可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
而关键字参数允许你传入0个或任意个含参数名的参数，
这些关键字参数在函数内部自动组装为一个dict。关键字参数有什么用？它可以扩展函数的功能
"""
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
person('Adam', 45, gender='M', job='Engineer')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **extra)

"""
命名关键字参数

对于关键字参数，函数的调用者可以传入任意不受限制的关键字参数。
至于到底传入了哪些，就需要在函数内部通过kw检查。
"""
def person(name, age, *, city, job):
    print(name, age, city, job)
person('Jack', 24, city='Beijing', job='Engineer')

"""
参数组合

在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，
这5种参数都可以组合使用。
但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
*args是可变参数，args接收的是一个tuple；
**kw是关键字参数，kw接收的是一个dict。
"""
def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f2(1, 2, d=99, ext=None)


###########################################################################################
from collections import Iterable
isinstance('abc', Iterable)  # str是否可迭代
isinstance([1, 2, 3], Iterable)  # list是否可迭代
isinstance(123, Iterable)  # 整数是否可迭代


"""
生成器generator

通过列表生成式，我们可以直接创建一个列表。
但是，受到内存限制，列表容量肯定是有限的。
而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，
如果我们仅仅需要访问前面几个元素，那后面绝大多数元素占用的空间都白白浪费了。

所以，如果列表元素可以按照某种算法推算出来，
那我们是否可以在循环的过程中不断推算出后续的元素呢？
这样就不必创建完整的list，从而节省大量的空间。
在Python中，这种一边循环一边计算的机制，称为生成器：generator
"""

L = [x * x for x in range(10)]  #
print(L)
# 创建了一个generator后，基本上永远不会调用next()，而是通过for循环来迭代它，
# 并且不需要关心StopIteration的错误
g = (x * x for x in range(10))
for n in g:
     print(n, end='')
"""
定义generator的另一种方法:
如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generato
"""
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n += 1
    return 'done'
# print(fib(5))  # <generator object fib at >0x0000029D7E6CC0F8
# g = fib(6)
# while True:
#     try:
#         x = next(g)
#         print('g:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

'''
函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
而变成generator的函数，在每次调用next()的时候执行，
遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
'''
# def triangles_YangHui(n):
#     count = 0
#     L = [1]
#     while True:
#         yield L
#         L.append(0)
#         L = [L[i-1] + L[i] for i in range(len(L))]
#         count += 1
#         if count == n:
#             break
# generator = triangles_YangHui(50)
# while True:
#     try:
#         x = next(generator)
#         print('generator:', x)
#     except StopIteration as e:
#         print('Generator return value:', e.value)
#         break

################################################################
# 小结
#
# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，
# 不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的，例如：

for x in [1, 2, 3, 4, 5]:
    pass
# 实际上完全等价于：
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break

"""
高阶函数：

既然变量可以指向函数，函数的参数能接收变量，
那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数
"""

def add(x, y, f):
    x = f(x) + f(y)
    return x
print(add(-3, 8, abs))  # 返回11

from functools import reduce
def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

print(reduce(fn, [1, 3, 5, 7, 9]))  # 13579
print(reduce(fn, map(char2num, '13579')))  # 将字符转换成整数
print(reduce(lambda x, y: x*10+y, map(char2num, '13579')))  # 将字符转换成整数
"""
惰性序列
filter()函数返回的是一个Iterator，也就是一个惰性序列，
所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
"""


# 找素数
def _odd_iter():  # 构造一个从3开始的奇数序列,因为素数都是奇数
    n = 1
    while True:
        n += 2
        yield n


def _not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = _odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的第一个数
        it = filter(_not_divisible(n), it)  # 过滤，构造新序列
        yield n
# 打印100以内的素数:
for n in primes():
    if n < 100:
        print(n, ' ', end='')
    # 2  3  5  7  11  13  17  19  23  29  31  37  41  43  47  53  59  61  67  71  73  79  83  89  97
    else:
        break

##########################################################################
"""
默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，
大写字母Z会排在小写字母a的前面。
现在，我们提出排序应该忽略大小写，按照字母序排序。
要实现这个算法，不必对现有代码大加改动，只要我们能用一个key函数把字符串映射为忽略大小写排序即可。
忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较
"""
# sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)


def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum  # 返回一个函数名
f = lazy_sum(1, 3, 5, 7, 9)
f()  # 调用时才返回求和值25