# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 10:47 '
"""
1.问题描述:
完全数（Perfect number)，又称完美数或完备数，
是一些特殊的自然数。它所有的真因子(即除了自身以外的约数）的和（即因子函数），
恰好等于它本身。例如，第一个完全数是6，它有约数1、2、3、6，除去它本身6外，
其余3个数相加，1+2+3=6。第二个完全数是28，它有约数1、2、4、7、14、28，
除去它本身28外，其余5个数相加，1+2+4+7+14=28。

编程求10000以内的完全数。
"""

#完全数6 = 1 + 2 + 3 + 6 - 6
#找所有的约数
# n = 24
# for i in range(1,n):#这个算法不够聪明，有点浪费了，重复循环了
#     if n % i == 0:
#         print(i)#找到24的所有的约数


#(1,24), (2,12), (3,8), (4,6), 之后都重复了(6,4), (8,3)
#找n的约数关键 ：a*b = n (a<=b)
def isPerfectNumber(n):
    a = 1
    b = n
    s = 0 #用来求和
    while a<b:
        if n%a == 0:
             s += a+b
        a +=1
        b = int(n/a)

    if a == b and a*b==n :
        s += a

    return s-n == n #s-n == n就是一个bool表达式，如果它成立的话，直接retrun true

    # if s-n == n:  #这种写法比较啰嗦
    #     return True
    # else:
    #     return False

# print(isPerfectNumber(28))#return True


#利用穷举法找2-10000以内的完全数
for i in range(2,10000):
    if isPerfectNumber(i):
        print(i)
#找到了4个完全数
# 6
# 28
# 496
# 8128



