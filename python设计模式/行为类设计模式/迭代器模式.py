# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/31 11:11'
# 生成器
# def MyGenerater(n):
#     index=0
#     while index<n:
#         yield index**2
#         index+=1
# if __name__=="__main__":
#     x_square=MyGenerater(10)
#     for x in x_square:
#         print x
# if __name__ == "__main__":
#     lst = ["hello Alice", "hello Bob", "hello Eve"]
#     lst_iter = iter(lst)
#     print lst_iter
#     print lst_iter.next()
#     print lst_iter.next()
#     print lst_iter.next()
#     # print lst_iter.next()

class MyIter(object):
    def __init__(self, n):
        self.index = 0
        self.n = n

    # def __iter__(self):
    #     return self

    def __iter__(self):
        return MyIter(self.n)  # 使得可以重复迭代

    def next(self):
        if self.index < self.n:
            value = self.index ** 2
            self.index += 1
            return value
        else:
            raise StopIteration()
#############################################


if __name__ == "__main__":
    x_square = MyIter(10)
    for x in x_square:
        print x
    for x in x_square:
        print x