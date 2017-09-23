# _*_ coding: utf-8 _*_


import random

"""
致筛子：玩家掷两个筛子，点数为1-6，
如果第一次点数之和为7或者11.则玩家胜利；

如果点数之和为2，3或者12，则玩家输；

如果和为其他点数，则记录第一次的点数和，继续掷筛子，
直到点数和等于第一次掷出的点数和，则玩家胜利；

如果在这之前掷出的点数和为7，则玩家输

没什么难度，只要用代码表达出文字的意思就行了
"""


def fun():
    k = random.randint(1, 6) + random.randint(1, 6)  # randint（1，6）包括了6
    if k in (7, 11):
        return True  # 玩家赢了
    if k in (2, 3, 12):
        return False  # 玩家输了

    while True:
        kk = random.randint(1, 6) + random.randint(1, 6)
        if kk == k:
            return True  # 玩家赢了
        if kk == 7:
            return False  # 玩家输了


print(fun())
