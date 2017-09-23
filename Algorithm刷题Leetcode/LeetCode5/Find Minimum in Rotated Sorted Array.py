# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 15:17'

def findMin(num):
    for i in range(len(num)):
        # if i == len(num) - 1:
        #     return num[i]
        if num[i] < num[i-1] and num[i] < num[i+1]:
            # 判断这个数 是否小于其前面一个数 和 其后面一个数
            if num[len(num) - 1] < num[i]:
                return num[len(num)-1]  # 如果最小的数在最后一位
            else:
                return num[i]
# l = [2, 9, 3, 5, 7, 5, 3, 9, 2]
l = [9, 3, 5, 7, 5, 3, 9]
print(findMin(l))
