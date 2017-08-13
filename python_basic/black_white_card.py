# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/9 10:16'


str = input()
nEventWhite = 0
nEventBlack = 0
nOddWhite = 0
nOddBlack = 0
for i in range(0, len(str)):
    if i%2 == 1:
        if str[i] == 'w':
            # print("change black into b")
            nOddWhite += 1

        else:
            # print("change white into b")
            nOddBlack += 1  # w

    else:
        if str[i] == 'w':
            # print("change white into b")
            nEventWhite += 1
        else:
            # print("change black into w")
            nEventBlack += 1

res = nOddBlack + nEventWhite
res1 = nOddWhite + nEventBlack
if res < res1:
    print(res)
else:
    print(res1)


#
# 1.定义四个变量
# nEvenWhite: 偶数位置白色个数
# nEvenBlack: 偶数位置黑色个数
# nOddWhite:  奇数位置白色个数
# nOddBlack:  奇数位置黑色个数
# 2.则最终
# 把偶数位置的白色变为黑色，奇数位置黑色变成白色
# 把奇数位置的白色变成黑色，偶数位置的黑色变成白色
# 3.结果即是上树两种结果最小值


"""
牛牛有n张卡片排成一个序列.每张卡片一面是黑色的,
另一面是白色的。初始状态的时候有些卡片是黑色朝上,有些卡片是白色朝上。
牛牛现在想要把一些卡片翻过来,得到一种交替排列的形式,即每对相邻卡片的颜色都是不一样的。
牛牛想知道最少需要翻转多少张卡片可以变成交替排列的形式。
"""