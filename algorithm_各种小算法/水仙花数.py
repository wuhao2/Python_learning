# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/7 15:18 '


# 水仙花数就是指一个n位数（n>=3)，它的每一位上的数字的n次幂之和等于它的本身
# eg: 1^3 + 5^3 + 3^3 = 153
# 求100-999之间所有的水仙花数

def isArmstrongNumber(n):
    list = []  # 153---->[3,1,5]
    temp = n  # 后面要用来比较，所以要赋值给一个临时变量，

    while temp > 0:
        list.append(temp % 10)  # 求余数
        temp = int(temp / 10)  # 153/10 = 15
    length = len(list)

    return sum([x ** length for x in list]) == n
    # python是高级语言，运用那个python列表解析和sum函数

    # sum = 0
    # for x in list:
    #     sum = sum + x**length
    # if sum == n:
    #     return sum
    # #return sum == n #优化代码,代码更加简洁


# 找出100到1000之间的所有的水仙花数
for x in range(100, 1000):
    if isArmstrongNumber(x):
        print(x)
