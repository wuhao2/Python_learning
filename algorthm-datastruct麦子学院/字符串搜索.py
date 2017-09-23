# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/7 20:40'

"""KMP算法----字符串搜索"""
def strstr(source, target):   # 复杂度为O(mn)
    """
    :param source:
    :param target:
    :return:
    """
    max = len(source) - len(target)
    for i in range(max + 1):  # 迭代寻找第一个相同的字符
        if source[i] == target[0]:
            j = 1
            while j < len(target) and source[i+j] == target[j]:
                j += 1
            if j == len(target):  # 说明target是source的子串
                return i
    return -1

s = "nihaowu"
t = "wu"
print(strstr(s, t))  # 返回子字符串的第一个索引
