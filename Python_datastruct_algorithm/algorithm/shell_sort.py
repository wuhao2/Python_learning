# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/16 13:01'
# 选择排序、快速排序、希尔排序、堆排序不是稳定的排序算法，
# 冒泡排序、插入排序、归并排序和基数排序是稳定的排序算法。


def shell_sort(lists):
    # 希尔排序
    count = len(lists)
    step = 2
    group = count / step
    while group > 0:
        for i in range(0, group):
            j = i + group
            while j < count:
                k = j - group
                key = lists[j]
                while k >= 0:
                    if lists[k] > key:
                        lists[k + group] = lists[k]
                        lists[k] = key
                    k -= group
                j += group
        group /= step
    return lists