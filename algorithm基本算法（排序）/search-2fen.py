# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 13:59 '

def binarySearchRescursive(list, x):
    """二分查找递归"""
    if len(list) == 0:
        return False  # 递归出口
    else:
        mid = len(list)//2
        if list[mid] == x:
            return True
        elif x < list[mid]:
            return binarySearchRescursive(list[:mid], x)
        else:
            return binarySearchRescursive(list[mid+1:], x)


def binarySearch(list, x):
    """二分查找非递归"""
    start = 0  # 头指针
    end = len(list) - 1  # 尾指针
    while start <= end:
        # 一次二分查找
        if start > end:
            print("searchdata not found ")
        middle = (start + end) // 2  # 中间指针
        if list[middle] == x:
            print("searchData is found", list[middle])
            return middle
        elif list[middle] > x:
            end = middle - 1
        elif list[middle] < x:
            start = middle + 1
    return False
if __name__ == "__main__":
    list = [1, 5, 8, 11, 56, 78, 90, 101, 111, 345]
    print(binarySearchRescursive(list, 56))
    print(binarySearchRescursive(list, 55))
    print("***"*20)
    print(binarySearch(list, 78))
# from random import randint
# list= [randint(1, 20) for _ in range(10)]
    # list = [1, 5, 8, 11, 56, 78, 90, 101, 111, 345]
    # middle = binarySearch(list, 11)
    # print("got it:", list[middle])
