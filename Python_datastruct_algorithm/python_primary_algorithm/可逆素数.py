# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/7 16:49 '

"""
解题思路： 1、用筛法找到900以内的素数表
          2、迭代所有的素数，是素数的，则检测它的反序数是否是素数
          3、2条件为真，则打印这两个素数
"""
def getPrimeTable(n):
    pt = [True]*n
    for p in range(2,n):
        if not pt[p]: continue
        for i in range(p*p, n, p):
            pt[i] = False
    return pt

def getReversePrime():
    pt = getPrimeTable(900)#先得到900以内的素数
    for p in range(10, 900):
        if not pt[p]: continue  #如果不是素数，继续下一次循环
        q = int(str(p)[::-1])#将一个数反序1234--->4321
        if p!=q and q < 900 and pt[q]:#如果q是素数，要过滤掉 209-->902， 222--->222的情况,
            pt[q] = False#避免重复查找113-- 反序->311   311--反序->113
            print(p,q)
#test
getReversePrime()