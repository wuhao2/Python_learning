# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/20 22:01'
# Python的functools模块提供了很多有用的功能，
# 其中一个就是  偏函数（Partial function）
import functools
int2 = functools.partial(int, base=2)  # 固定传入base=2这个关键字参数
max2 = functools.partial(max, 10)
print(int2('1000000'))  # 64
print(max2(5, 6, 7))  # 10

"""
python内置函数，自定义函数不要与这些内置函数重名
            Built-in Functions
abs()	dict()	help()	min()	setattr()
all()	dir()	hex()	next()	slice()
any()	divmod()	id()	object()	sorted()
ascii()	enumerate()	input()	oct()	staticmethod()
bin()	eval()	int()	open()	str()
bool()	exec()	isinstance()	ord()	sum()
bytearray()	filter()	issubclass()	pow()	super()
bytes()	float()	iter()	print()	tuple()
callable()	format()	len()	property()	type()
chr()	frozenset()	list()	range()	vars()
classmethod()	getattr()	locals()	repr()	zip()
compile()	globals()	map()	reversed()	__import__()
complex()	hasattr()	max()	round()
delattr()	hash()	memoryview()	set()
"""

class Student(object):
    pass
s = Student()
s.name = 'wuhao'  # 动态给实例绑定一个属性
print(s.name)


def set_age(self, age):   # 定义一个函数作为实例方法
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)  # # 给实例绑定一个方法
s.set_age(25)  # 调用实例方法
print(s.age)  # 但是，给一个实例绑定的方法，对另一个实例是不起作用的：

def set_score(self, score):
    self.score =score
Student.set_score = set_score  # 给class绑定方法后，所有实例均可调用

s2 = Student()
s.set_score(100)
s2.set_score(99)

print(s.score, s2.score)  # 100  99

"""
使用__slots__

但是，如果我们想要限制实例的属性怎么办？
比如，只允许对Student实例添加name和age属性。
为了达到限制的目的，Python允许在定义class的时候，
定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
"""
class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

"""
设置分数时，可以对参数进行检查，复杂不优雅
"""
class Student(object):

    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

"""
装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
Python内置的@property装饰器就是负责把一个方法变成属性调用的
"""
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value
# birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。
    @property
    def age(self):
        return 2015 - self._birth

s = Student()
s.score = 78
s.score = 9999  # ValueError: score must between 0 ~ 100!