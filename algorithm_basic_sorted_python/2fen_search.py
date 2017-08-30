# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 13:59 '
from random import randint


# （折半）二分查找，也叫折半搜索法，必须先排好序
def twoFenSearch(list, x):
    start = 0  # 头指针
    end = len(list) - 1  # 尾指针
    for k in range(int(end / 2) + 1):
        # 一次二分查找
        if start > end:
            print("searchdata not found ")
        middle = int((start + end) / 2)  # 中间指针
        if list[middle] == x:
            print("searchData is found", list[middle])
            return middle
        elif list[middle] > x:
            end = middle - 1
        elif list[middle] < x:
            start = middle + 1


# list= [randint(1, 20) for _ in range(10)]
list = [1, 5, 8, 11, 56, 78, 90, 101, 111, 345]
middle = twoFenSearch(list, 11)
print("got it:", list[middle])
