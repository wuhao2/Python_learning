# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/10 15:51'


def getUgleNum(index):
    if index == 0:
        return 0
    count = 1
    index2 = 0
    index3 = 0
    index5 = 0
    num = 1
    ugleNum = [0 for i in range(index)]
    ugleNum[0] = 1
    while count < index:
        tmp2 = ugleNum[index2] * 2
        tmp3 = ugleNum[index3] * 3
        tmp5 = ugleNum[index5] * 5
        num = min(tmp2, min(tmp3, tmp5))
        ugleNum[count] = num

        while ugleNum[index2] * 2 <= ugleNum[count]:
            index2 += 1
        while ugleNum[index3] * 3 <= ugleNum[count]:
            index3 += 1
        while ugleNum[index5] * 5 <= ugleNum[count]:
            index5 += 1
        count += 1
    return num

print(getUgleNum(10))