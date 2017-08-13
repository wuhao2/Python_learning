# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/16 13:14'


def insert_sort(lists):
    # 插入排序
    count = len(lists)
    for i in range(1, count):
        key = lists[i]
        j = i - 1  # 表示当前数的前一个数的索引
        while j >= 0:
            if lists[j] > key:   # 插入过程：将当前数，一次与前面的数比较，插入到合适的位置
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1  # 循环条件
    return lists

lists = [3, 2, 4, 1, 59, 23, 13, 11, 34]
print(insert_sort(lists))
