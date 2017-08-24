# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/7 16:36 '
#因为除法很影响效率
#建一张表代替除法
"""
筛法找素数：1、建立一张表，用True，False标志一个数是否是素数
2、找到一个素数p，然后把p的倍数都标记为非素数
3、查表检测p+1，如果非素数检测下一个，是素数执行1的操作
"""

#2, 4, 6, 8, 10
#3，9，12，15
#6,12,15



def findPrime():
    """
    当数值很大的时候，就体现出了这个查表得优势
    :return:
    """
    primeTable = [True] * 100  # 定义一张素数表，初始化全部为True
    res = []

    for p in range(2, 100):
        if not primeTable[p]: continue#如果不是素数，继续下一次循环
        res.append(p)#是素数，并放入res列表中

        #用for循环产生所有的非素数
        for i in range(p*p,100,p):#筛选，起始p*p, 末尾100， 间隔是p
            primeTable[i] = False#标志出不是素数

    print(res)#所有的素数都在res中了

    for i in range(1, len(res)):
        if res[i] -res[i-1] == 2:
            print(res[i-1], res[i])#孪生素数，就是相邻的素数


#test
findPrime()