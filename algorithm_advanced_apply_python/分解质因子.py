# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 20:32 '


# 24 = 2*12 = 2* 2*6 = 2* 2* 2*3
# 解题思路：从k=2开始分解，然后对n/2又从k=2开始分解，依次类推

def primeFactors(n):
    k = 2
    while k <= n:
        if n % k == 0:
            print(k, "*", end='')
            n = n / k
        else:
            k += 1


primeFactors(90)
