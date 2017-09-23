# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/2 13:30 '


# 快速排序要点：1、选择基准数据 2、left和right指针和 活动指针的交叉移动
############################################################################

def quick_sort(alist, start, end):
    """快速排序"""
    # 递归的退出条件
    if start >= end:
        return
    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]
    # low为序列左边的由左向右移动的游标
    low = start
    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:  # 此大循环表示，low与high交替执行

        # 如果low与high未重合，high指向的元素不比基准元素小，
        while low < high and alist[high] >= mid:
            high -= 1  # 则high向左移动
        # 退出while时，将high指向的元素放到low的位置上------遇到了一个比mid小的数
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，
        while low < high and alist[low] < mid:
            low += 1  # 则low向右移动
        # 将low指向的元素放到high的位置上------遇到一个大于mid的数
        alist[high] = alist[low]


    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low - 1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low + 1, end)


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(alist, 0, len(alist) - 1)
print(alist)
"""O(nlogn)-----O(n^2)   不稳定---看应用场景，如果不需要保序，肯定选择快排"""



