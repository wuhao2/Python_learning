# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/31 9:53'


# 假设有一个网上咖啡选购平台，客户可以在该平台上下订单订购咖啡，
# 平台会根据用户位置进行线下配送。假设其咖啡对象构造如下：
class Coffee:
    name = ''
    price = 0

    def __init__(self, name):
        self.name = name
        self.price = len(name)
        # 在实际业务中，咖啡价格应该是由配置表进行配置，或者调用接口获取等方式得到，此处为说明享元模式，将咖啡价格定为名称长度，只是一种简化

    def show(self):
        print("Coffee Name:%s Price:%s" % (self.name, self.price))


# 其对应的顾客类如下：
# class Customer:
#     name = ""
#
#     def __init__(self, name):
#         self.name = name
#
#     def order(self, coffee_name):
#         print("%s ordered a cup of coffee:%s" % (self.name, coffee_name))
#         return Coffee(coffee_name)
#

'''重新定义咖啡类'''


class CoffeeFactory():
    coffee_dict = {}

    def getCoffee(self, name):
        if not self.coffee_dict.has_key(name):  ######################
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def getCoffeeCount(self):
        return len(self.coffee_dict)


class Customer:
    coffee_factory = ""
    name = ""

    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory

    def order(self, coffee_name):
        print("%s ordered a cup of coffee:%s" % (self.name, coffee_name))
        return self.coffee_factory.getCoffee(coffee_name)


if __name__ == "__main__":
    coffee_factory = CoffeeFactory()
    customer_1 = Customer("A Client", coffee_factory)
    customer_2 = Customer("B Client", coffee_factory)
    customer_3 = Customer("C Client", coffee_factory)
    c1_capp = customer_1.order("cappuccino")
    c1_capp.show()
    c2_mocha = customer_2.order("mocha")
    c2_mocha.show()
    c3_capp = customer_3.order("cappuccino")
    c3_capp.show()
    print("Num of Coffee Instance:%s" % coffee_factory.getCoffeeCount())

if __name__ == "__main__":
    coffee_factory = CoffeeFactory()
    customer_1 = Customer("A Client", coffee_factory)
    customer_2 = Customer("B Client", coffee_factory)
    customer_3 = Customer("C Client", coffee_factory)
    c1_capp = customer_1.order("cappuccino")
    c1_capp.show()
    c2_mocha = customer_2.order("mocha")
    c2_mocha.show()
    c3_capp = customer_3.order("cappuccino")
    c3_capp.show()
    print("Num of Coffee Instance:%s" % coffee_factory.getCoffeeCount())
