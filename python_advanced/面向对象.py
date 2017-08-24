# coding: utf-8
class Animal(object):
    pass
# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 特殊功能类
class Runnable(object):  # 能跑的类
    def run(self):
        print('Running...')
class Flyable(object):  # 能飞的类
    def fly(self):
        print('Flying...')


# 各种动物: 采用多重继承实现 能跑与能飞 的功能
class Dog(Mammal, Runnable):
    pass
class Bat(Mammal, Flyable):
    pass
class Parrot(Bird, Flyable):
    pass
class Ostrich(Bird, Runnable):
    pass
class Student(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object (name: %s)' % self.name
    # __repr__ = __str__  # 偷懒的写法
    def __repr__(self):
        return 'Student object (name: %s)' % self.name
"""
# 两者的区别是__str__()返回用户看到的字符串，
# 而__repr__()返回程序开发者看到的字符串，
# 也就是说，__repr__()是为调试服务的。
"""
print(Student('Michael'))  # Student object (name: Michael)
s = Student('Michael')
print(s)  # Student object (name: Michael)

"""
__iter__

如果一个类想被用于for ... in循环，类似list或tuple那样，
就必须实现一个__iter__()方法，该方法返回一个迭代对象，
然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，
直到遇到StopIteration错误时退出循环。
"""
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器a，b

    def __iter__(self):
        return self  # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 100:  # 退出循环的条件
            raise StopIteration()
        return self.a  # 返回下一个值

# for i in Fib():
#     print(i)

"""
__getitem__

Fib实例虽然能作用于for循环，看起来和list有点像，
但是，把它当成list来使用还是不行，比如，取第5个元素：
"""
class Fib1(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f = Fib1()
print(f[1])
print(f[4])
print(f[7])
print(f[0:5])

# 错误信息很清楚地告诉我们，没有找到score这个attribute。
# 要避免这个错误，除了可以加上一个score属性外，
# Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性。修改如下：
# 注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，不会在__getattr__中查找。

class Student(object):

    def __init__(self):
        self.name = 'Michael'

    def __getattr__(self, attr):
        if attr == 'score':
            return 99

    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)


# 利用完全动态的__getattr__，我们可以写出一个链式调用：
# 这样，无论API怎么变，SDK都可以根据URL实现完全动态的调用，而且，不随API的增加而改变！
class Chain(object):

    def __init__(self, path=''):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path
    def __repr__(self):
        return self._path
    # __repr__ = __str__

Chain().status.user.timeline.list


"""
__call__
一个对象实例可以有自己的属性和方法，当我们调用实例方法时，
我们用instance.method()来调用。能不能直接在实例本身上调用呢？在Python中，答案是肯定的。
任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用。请看示例：
通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。
"""
class Student3(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)
s3 = Student3('wuhao')
s3()  # My name is wuhao.


####################################################################################
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样我们就获得了Month类型的枚举类，可以直接使用Month.Jan来引用一个常量，或者枚举它的所有成员：

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
# value属性则是自动赋给成员的int常量，默认从1开始计数。

# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0  # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6

day1 = Weekday.Mon
print(day1.value)
for name, member in Weekday.__members__.items():
    print(name, '=>', member)

