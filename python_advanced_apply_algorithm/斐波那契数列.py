# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 13:22 '

def fibnacci(n):
    a = [1]*n
    for i in range(2,n):
        a[i] = a[i-1] + a[i-2]
    return a

print(fibnacci(20))

def fibnacci1(n):
    res = []
    a,b = 0,1
    while b<n:
        res.append(b)
        a,b = b,a+b
    return res
#test
fib = fibnacci1(20)
print(fib)

