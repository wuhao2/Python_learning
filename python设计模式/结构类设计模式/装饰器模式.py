# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/31 9:03'
class LogManage:
    @staticmethod
    def log(func):
        def wrapper(*args, **kw):
            print('call %s():' % func.__name__)
            return func(*args, **kw)
        return wrapper

class Beverage():
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class coke(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


class drinkDecorator():
    def getName(self):
        pass

    def getPrice(self):
        pass


class iceDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    @LogManage.log
    def getName(self):
        return self.beverage.getName() + " +ice"
    @LogManage.log
    def getPrice(self):
        return self.beverage.getPrice() + 0.3


class sugarDecorator(drinkDecorator):
    def __init__(self, beverage):
        self.beverage = beverage
    @LogManage.log
    def getName(self):
        return self.beverage.getName() + " +sugar"
    @LogManage.log
    def getPrice(self):
        return self.beverage.getPrice() + 0.5

if __name__ == "__main__":
    coke_cola = coke()
    print("Name:%s" % coke_cola.getName())
    print("Price:%s" % coke_cola.getPrice())
    ice_coke = iceDecorator(coke_cola)
    print("Name:%s" % ice_coke.getName())
    print("Price:%s" % ice_coke.getPrice())

################################################################################



# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
# @log
# def now():
#     print('2016-12-04')
# if __name__ == "__main__":
#     now()



