# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/9 20:31'

"""类属性"""
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0, -4.5)
# print(x.i, x.r)


""" 类定义"""


class people(object):
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法

    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("{0} is speaking: I am {age} years old".format(self.name, age=self.age))


# p = people('tom', 10, 30)
# p.speak()

"""单继承示例"""
class student(people):
    grade = ''

    def __init__(self, n, a, w, g):
        # 调用父类的构函
        people.__init__(self, n, a, w)
        self.grade = g

    # 覆写父类的方法
    def speak(self):
        print("%s is speaking: I am %d years old,and I am in grade %d" % (self.name, self.age, self.grade))


# s = student('ken', 20, 60, 3)
# s.speak()


class speaker(object):
    topic = ''
    name = ''

    def __init__(self, n, t):
        self.name = n
        self.topic = t

    def speak(self):
        print("I am %s,I am a speaker!My topic is %s" % (self.name, self.topic))


"""
多重继承
需要注意圆括号中父类的顺序，若是父类中有相同的方法名，而在子类使用时未指定，
python从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法
"""


class sample(speaker, student):
    a = ''

    def __init__(self, n, a, w, g, t):
        student.__init__(self, n, a, w, g)
        speaker.__init__(self, n, t)


test = sample("Tim", 25, 80, 4, "Python")
test.speak()  # 方法名同，默认调用的是在括号中排前地父类的方法

"""
类私有方法
__private_method 两个下划线开头，声明该方法为私有方法，不能在类地外部调用。

在类的内部调用slef.__private_methods。

类的专有方法：

__init__ 构造函数，在生成对象时调用
__del__ 析构函数，释放对象时使用
__repr__ 打印，转换
__setitem__按照索引赋值
__getitem__按照索引获取值
__len__获得长度
__cmp__比较运算
__call__函数调用
__add__加运算
__sub__减运算
__mul__乘运算
__div__除运算
__mod__求余运算
__pow__称方
"""
