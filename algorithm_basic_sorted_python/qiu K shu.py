# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/26 16:37'

from random import randint


def find_Kth_Max(list, k):
    if k > len(list):
        return
    key = randint(0, len(list) - 1)
    key_value = list[key]
    sl = [i for i in list[:key] + list[key + 1:] if i < key_value]
    bl = [i for i in list[:key] + list[key + 1:] if i >= key_value]
    if len(bl) == k - 1:
        return key_value
    elif len(bl) >= k:
        return find_Kth_Max(bl, k)
    else:
        return find_Kth_Max(sl, k - len(bl) - 1)


if __name__ == '__main__':
    array = [45, 67, 33, 21]
    th = find_Kth_Max(array, 3)
    print(th)
