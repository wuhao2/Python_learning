# coding:utf-8
__author__ = 'wuhao'
__date__ = '2017/7/16 13:01'

"""
# 选择排序、快速排序、希尔排序、堆排序是 不稳定 的排序算法，
# 冒泡排序、插入排序、归并排序和基数排序是  稳定  的排序算法。

"""
def shell_sort(alist):
    n = len(alist)
    # 初始步长 9//2=4
    gap = n // 2
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):  # [gap, gap+1, gap+2 ..... n]一次循环将这些都完成了
            j = i

            # 插入排序
            while j > 0:
                if alist[j - gap] > alist[j]:  # 相当于插入交换
                    alist[j - gap], alist[j] = alist[j], alist[j - gap]
                    j -= gap
                else:
                    break

        # while循环条件,得到新的步长
        gap //= 2


alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]  # 不稳定   最优O(n^1.3)---最坏O(n^2)
shell_sort(alist)
print(alist)
