# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/7 19:49'

"""递归折半搜索"""
def binarySearch(list, key, begin, end):
    # begin = 0
    # end = len(list)-1
    if begin > end:
        print("not found")
        return
    mid = int((begin + end) / 2)
    if list[mid] > key:
        return binarySearch(list, key, begin, mid-1)
    elif list[mid] < key:
        return binarySearch(list, key, mid+1, end)
    else:
        return list[mid]


"""非递归实现"""
def binarySearchNonRecursive(list, key):
    left = 0
    right = len(list)-1
    while left <= right:
        mid = int((left+right)/2)
        if key > list[mid]:
            left = mid + 1
        if key < list[mid]:
            right = mid -1
        if key == list[mid]:
            print("found: ", list[mid])
            return list[mid]
    print("not found")


a = [1, 3, 5, 7, 9, 32, 99]  # 已经排好序的
binarySearchNonRecursive(a, 99)