# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 17:02 '


def yang(floor):
    now = []
    for x in range(1, floor + 1):
        now.append(x)
        for index in range(len(now) - 2, 0, -1):
            now[index] = now[index - 1] + now[index]
            # 上一行的相邻的两个数之和等下一行的数
        print(now)


yang(7)
