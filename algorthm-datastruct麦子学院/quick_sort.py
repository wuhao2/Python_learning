# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/7 19:14'
"""递归实现"""
def quick_sort(list, begin, end):
    if begin >= end:
        return  # 递归出口
    left = begin
    right = end
    pivotValue = list[left]  # 第一个元素做轴
    while left < right:
        if list[left + 1] < pivotValue:
            list[left] = list[left + 1]
            left += 1
        else:
            list[left + 1], list[right] = list[right], list[left + 1]
            right -= 1
    list[left] = pivotValue
    quick_sort(list, begin, left-1)  # 左边继续排序
    quick_sort(list, left+1, end)  # 右边在继续排序
    return list

a = [1, 8, 3, 5, 2, 9, 7]
begin = 0
end = len(a) - 1
print(quick_sort(a, begin, end))
