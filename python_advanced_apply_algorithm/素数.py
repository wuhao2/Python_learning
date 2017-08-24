# _*_ coding: utf-8 _*_


__author__ = 'bobby'
__data__ = '2017/6/9 15:32 '
"""
1.问题描述:
素数（质数）指的是不能被分解的数，除了1和它本身之外就没有其他数能够整除。
求100以内的所有素数。
"""

"""
def isPrimeNumber(n):
    for i in range(2,n):
        if n % i == 0: return False
        else:
            return True
# #test
# res = isPrimeNumber(97)
# print('res:', res) #成功完成功能
"""


"""
import math
def isPrimeNumber1(n): #优化，上面的函数每次要遍历一遍，效率不高
    for i in range(2, int(math.sqrt(n) + 1)):#其实只需要让n除以 2到int(math.sqrt(n) + 1)，不需要要除以 2到n，效率提高了
        if n % i == 0: return False
        else:
            return True
#test
res = isPrimeNumber1(97)
print('res:', res) #成功完成功能
"""



def isPrimeNumber2(n, prime):#再次优化，其实只需要让k在prime的集合中循环即可
    for k in prime:
        if k * k > n: break
        if n % k == 0: return None
    return n
prime = []
for n in range(2, 100):
    res = isPrimeNumber2(n, prime)
    if res: prime.append(res)
print (prime)
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

