# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/16 13:14'
# 最优O(n)  最坏O(n^2)  稳定的
# 前面无序， 后面是有序的，将后面的依次插入到前面

def insert_sort(alist):
    # 从第二个位置，即下标为1的元素开始向前插入
    for i in range(1, len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，交换位置
        for j in range(i, 0, -1):  # 在前面i个已经排好序的序列中，从后往前比较
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]
            else:  # 优化
                break  # 正好大于前面的那个数，就不需要比较，退出内层循环

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insert_sort(alist)
print(alist)
