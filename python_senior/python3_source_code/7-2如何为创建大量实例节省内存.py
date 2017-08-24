# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 18:34'


class Player(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level


class Player2(object):
    __slots__ = ['uid', 'name', 'stat', 'level']
    # 阻止动态绑定额外的属性，节省内存

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.stat = status
        self.level = level

p1 = Player('0001', 'Jim')
p2 = Player2('0002', 'Tom')
print(set(dir(p1))-set(dir(p2)))
print(p1.__dict__)
# print(p2.__dict__)  p2没有属性__dict__
p1.x = 123
print(p1.__dict__)
del p1.__dict__['x']
print(p1.__dict__)


import sys
memory_size = sys.getsizeof(p1.__dict__)
print(memory_size)  # 320byte
