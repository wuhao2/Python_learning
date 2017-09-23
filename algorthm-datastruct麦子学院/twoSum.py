# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/7 21:06'

"""两个数的和 O(n^2)"""
def twoSum(list, target):
    for i in range(len(list)):
        for j in range(i+1, len(list)):  # 消除重复1 8 、 8 1的情况
            if list[i] + list[j] == target:
                print(list[i], list[j])

"""对于一个已经排好序的数组  O(n)"""
def twoSumSorted(list, target):
    left = 0
    right = len(list)-1
    while left < right:
        sum = list[left] + list[right]
        if target < sum:
            right -= 1
        if target > sum:
            left += 1
        else:
            '''此处存在一个严重的bug，导致死循环'''
            print(list[left], list[right])
            left += 1
            right -= 1  # 循环条件

a = [0, 1, 3, 5, 6, 4, 2, 7, 8, 9]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(twoSum(a, 8))
# print(twoSumSorted(b, 9))

def threeSum(num):
    num.sort()
    res = []
    for i in range(len(num)-2):
        if i == 0 or num[i] > num[i-1]:
            left = i + 1
            right = len(num) - 1
            while left < right:
                if num[left] + num[right] == -num[i]:
                    res.append([num[i], num[left], num[right]])
                    left += 1
                    right -= 1
                    while left < right and num[left] == num[left-1]:
                        left +=1
                    while left < right and num[right] == num[right+1]:
                        right -= 1
                elif num[left] + num[right] < -num[i]:
                    while left < right:
                        left += 1
                        if num[left] > num[left-1]:
                            break
                else:
                    while left < right:
                        right -= 1
                        if num[right] < num[right+1]:
                            break
    return res
from random import randint
# c = [randint(0, 9) for _ in range(9)]
c = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(threeSum(c))
