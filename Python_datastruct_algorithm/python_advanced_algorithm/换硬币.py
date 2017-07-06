# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 17:20 '
"""
问题描述:
设有n种不同面值的硬币，各硬币的面值存于数组w[i]中。现要用这些面值的硬币来找钱，
可以使用的各种面值的硬币个数存于数组S[i]中。

对任意钱数0≤m,设计一个用最少硬币找钱m的方法
"""
#解题思路： 1、贪心算法，优先选择面值大的找钱  2、直到凑成需要的钱数 3、字典存储每种面值的个数
#返回{10：2， 5：2， 2：4， 1：2}

w = [10, 5, 2, 1]  #硬币的面值
s = [2, 7, 4, 3]  #硬币个数

def changeMoney(n):
    res = {}
    for v,c in zip(w,s):
        k = min( int(n/v), c )
        if k > 0:
            res[v] = k

        n -= k*v
        if n == 0: break
    return res if n == 0 else None#如果最后正好n=0，说明，正好找开了，

print(changeMoney(49))  #返回{10: 2, 2: 2, 5: 5}即49=10*2 + 2*2 + 5*5
print(changeMoney(13))  #返回{1: 1, 10: 1, 2: 1}
print(changeMoney(8))  #返回{1: 1, 2: 1, 5: 1}