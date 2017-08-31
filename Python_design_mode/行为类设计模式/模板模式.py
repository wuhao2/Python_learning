# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/31 13:08'


# 根据股票代码来查询股价分为如下几个步骤：登录、设置股票代码、查询、展示。
# 构造如下的虚拟股票查询器：
class StockQueryDevice():
    stock_code = "0"
    stock_price = 0.0

    def login(self, usr, pwd):
        pass

    def setCode(self, code):
        self.stock_code = code

    def queryPrice(self):
        pass

    def showPrice(self):
        pass
# 每次操作，都会调用登录，设置代码，查询，展示这几步，是不是有些繁琐？
# 既然有些繁琐，何不将这几步过程封装成一个接口。
# 由于各个子类中的操作过程基本满足这个流程，所以这个方法可以写在父类中：

class StockQueryDevice():
    stock_code="0"
    stock_price=0.0
    def login(self,usr,pwd):
        pass
    def setCode(self,code):
        self.stock_code=code
    def queryPrice(self):
        pass
    def showPrice(self):
        pass
    # def operateQuery(self,usr,pwd,code):
    #     self.login(usr,pwd)
    #     self.setCode(code)
    #     self.queryPrice()
    #     self.showPrice()
    #     return True
    def operateQuery(self,usr,pwd,code):
        if not self.login(usr,pwd):
            return False
        self.setCode(code)
        self.queryPrice()
        self.showPrice()
        return True
# 现在查询机构很多，我们可以根据不同的查询机构和查询方式，来通过继承的方式实现其对应的股票查询器类。
# 例如，WebA和WebB的查询器类可以构造如下：
class WebAStockQueryDevice(StockQueryDevice):
    def login(self, usr, pwd):
        if usr == "myStockA" and pwd == "myPwdA":
            print "Web A:Login OK... user:%s pwd:%s" % (usr, pwd)
            return True
        else:
            print "Web A:Login ERROR... user:%s pwd:%s" % (usr, pwd)
            return False

    def queryPrice(self):
        print "Web A Querying...code:%s " % self.stock_code
        self.stock_price = 20.00

    def showPrice(self):
        print "Web A Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price)


class WebBStockQueryDevice(StockQueryDevice):
    def login(self, usr, pwd):
        if usr == "myStockB" and pwd == "myPwdB":
            print "Web B:Login OK... user:%s pwd:%s" % (usr, pwd)
            return True
        else:
            print "Web B:Login ERROR... user:%s pwd:%s" % (usr, pwd)
            return False

    def queryPrice(self):
        print "Web B Querying...code:%s " % self.stock_code
        self.stock_price = 30.00

    def showPrice(self):
        print "Web B Stock Price...code:%s price:%s" % (self.stock_code, self.stock_price)


# 在场景中，想要在网站A上查询股票，需要进行如下操作：

# if __name__ == "__main__":
#     web_a_query_dev = WebAStockQueryDevice()
#     web_a_query_dev.login("myStockA", "myPwdA")
#     web_a_query_dev.setCode("12345")
#     web_a_query_dev.queryPrice()
#     web_a_query_dev.showPrice()




if  __name__=="__main__":
    web_a_query_dev=WebAStockQueryDevice()
    web_a_query_dev.operateQuery("myStockA","myPwdA","12345")