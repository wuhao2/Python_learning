# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 10:42'
"""
给定一个数组（列表），找到这个列表中的主元素，
所谓主元素就是该元素在列表中出现的次数大于n/2，
n为该数组的长度。这里提供两种方法：

第一种首先将数组排序，
那么中间的那个数num[n//2]必然就是主元素了，因为主元素的个数要大于整个数组长度的一般嘛，
O(nlogn)的复杂度；

第二种方法是用字典来存储每个数出现的次数，
当某个键值的次数大于一般是即返回，O(n)的复杂度。
"""
def majorityElement1(num):
    """
    :param num:  a list of integer
    :return:  an integer
    """
    num.sort()
    return num[len(num)//2]

# Another version -- Hash
def majorityElement2(num):
    dic = {}
    for i in range(len(num)):
        if num[i] in dic.keys():
            dic[num[i]] += 1
            if dic[num[i]] > len(num)//2:
                return num[i]
        else:
            dic[num[i]] = 1
            if dic[num[i]] > len(num)//2:
                return num[i]

num = {2, 6, 2, 2, 9, 1, 4, 8, 2, 5, 2, 3, 2, 5, 2, 3, 3, 2, 3}

print(majorityElement2(num))