# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/10 15:43'
from random import randint

def inputData(n):
    data = [randint(0, n) for _ in range(20, n)]
    data30 = [randint(0, 20) for _ in range(20)]
    data100 = data30+data
    print(len(data100))
    print(data100)

    return data100

def output(list):
    res = []
    count = 0
    for i in list:
        for j in list:
            if i == j:
                print([res.append(i)])
                count += 1
                continue
    return count

dataList = inputData(30)
print(output(dataList))
