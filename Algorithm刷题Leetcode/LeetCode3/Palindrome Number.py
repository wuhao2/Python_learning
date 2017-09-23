# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 8:38'

# @return a boolean
def isPalindrome(x):
    mode, result = 1, True
    while x//mode >= 10:  # 相当于算出有多少位
        mode *= 10
    while x:
        if x // mode != x % 10:
            result = False
            return result
        x -= mode*(x//mode)
        x //= 10
        mode //= 100
    return result
print(isPalindrome(12321))