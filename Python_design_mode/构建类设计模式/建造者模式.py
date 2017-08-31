# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/30 21:50'


# 今天的例子，还是上一次谈到的快餐点餐系统。只不过，今天我们从订单的角度来构造这个系统。
# 最先还是有请上次的主角们：
# 主餐：

class Burger():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class cheeseBurger(Burger):
    def __init__(self):
        self.name = "cheese burger"
        self.price = 10.0


class spicyChickenBurger(Burger):
    def __init__(self):
        self.name = "spicy chicken burger"
        self.price = 15.0


# 小食：

class Snack():
    name = ""
    price = 0.0
    type = "SNACK"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class chips(Snack):
    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):
    def __init__(self):
        self.name = "chicken wings"
        self.price = 12.0


# 饮料：

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


# 最终，我们是要建造一个订单，因而，需要一个订单类。假设，一个订单，
# 包括一份主食，一份小食，一种饮料。（省去一些异常判断）

class order():
    burger = ""
    snack = ""
    beverage = ""

    def __init__(self, orderBuilder):
        self.burger = orderBuilder.bBurger
        self.snack = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print("Burger:%s" % self.burger.getName())
        print("Snack:%s" % self.snack.getName())
        print("Beverage:%s" % self.beverage.getName())


# 代码中的orderBuilder是什么鬼？这个orderBuilder就是建造者模式中所谓的“建造者”了，
# 先不要问为什么不在order类中把所有内容都填上，而非要用builder去创建。接着往下看。
# orderBuilder的实现如下：

class orderBuilder():
    bBurger = ""
    bSnack = ""
    bBeverage = ""

    def addBurger(self, xBurger):
        self.bBurger = xBurger

    def addSnack(self, xSnack):
        self.bSnack = xSnack

    def addBeverage(self, xBeverage):
        self.bBeverage = xBeverage

    def build(self):
        return order(self)


'''
在建造者模式中，还可以加一个Director类，用以安排已有模块的构造步骤。
对于在建造者中有比较严格的顺序要求时，
该类会有比较大的用处。在上述例子中，Director实现如下：
'''


class orderDirector():
    order_builder = ""

    def __init__(self, order_builder):
        self.order_builder = order_builder

    def createOrder(self, burger, snack, beverage):
        self.order_builder.addBurger(burger)
        self.order_builder.addSnack(snack)
        self.order_builder.addBeverage(beverage)
        return self.order_builder.build()


# 在场景中如下去实现订单的生成：

if __name__ == "__main__":
    order_builder = orderBuilder()

    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(chips())
    order_builder.addBeverage(milk())

    order_1 = order_builder.build()
    order_1.show()
