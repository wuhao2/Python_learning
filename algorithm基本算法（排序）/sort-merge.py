# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/18 16:00'

# 稳定 O（nlogn)-----O(n^2)
def merge_sort(alist):
    if len(alist) <= 1:  # 递归出口--即拆分到只有一个元素
        return alist
    # 二分分解
    num = len(alist) // 2
    left = merge_sort(alist[:num])  # left中接收  merge_sort左边返回的有序序列
    right = merge_sort(alist[num:])  # right中接收  merge_sort右边返回的有序序列

    '''合并操作，将两个有序数组left[]和right[]合并成一个大的有序数组'''
    l, r = 0, 0  # left与right的下标指针
    result = []  # 用来保存合并后的新列表
    while l < len(left) and r < len(right):  # 谁小，谁就放入result，然后指针+1
        if left[l] <= right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    result += left[l:]  # ？？如果左边走到头
    result += right[r:]  # ？？如果是右边走到头
    return result

if __name__ == "__main__":
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    print(alist)
    sorted_alist = merge_sort(alist)
    print(alist)
    print("sorted_alist:", sorted_alist)  # ；拿到的是一个新的列表，空间上有额外的开销
