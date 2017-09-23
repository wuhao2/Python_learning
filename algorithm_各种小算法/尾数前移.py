# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/7 14:49 '

"""
尾数前移
解题思路：1236--->6123 == 4*1236
"""


def fun(n):
    nn = n
    t = 6
    while nn > 0:
        t *= 10
        nn = int(nn / 10)
    # print('t=',t) #此时t=6000

    m = 10 * n + 6  # n=123，则m= 123*10 +6 = 1236
    if t + n == m * 4:
        print(m)


# print(fun(123))
for x in range(1, 100000):  # 穷举法
    fun(x)
# 得到153846
