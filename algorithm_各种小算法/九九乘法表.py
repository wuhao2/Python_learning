# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 16:59 '


def fun():
    for line in range(1, 10):
        for row in range(1, line + 1):
            print(str(line) + '*' + str(row) + '=' + str(line * row), '\t', end='')  # 不换行
        print()  # 换行
# test
fun()