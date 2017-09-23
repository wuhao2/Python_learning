# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 16:52'
from abc import ABCMeta, abstractmethod

class SimpleAbstractClass(metaclass=ABCMeta):
    pass
SimpleAbstractClass.register(list)  # 将list注册成抽象基类
assert isinstance([], SimpleAbstractClass)

######################################################
class abstract(metaclass=ABCMeta):
    @abstractmethod
    def absMeta(self):
        pass
class A(abstract):
    def absMeta(self):
        print("implement abstract method")
        return 0
A().absMeta()
