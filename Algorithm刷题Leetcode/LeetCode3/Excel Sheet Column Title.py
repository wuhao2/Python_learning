# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 10:15'
"""
给定一个数字，将其转换为Excel的title，其实就相当于把一个数转化为26进制的数。
"""
def convertToTitle(num):
    dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ''
    while num:
        result += dic[(num - 1) % 26]  # 取余数
        num = (num - 1) // 26  # 取商（int）
    return result[::-1]  # 将ZH变成HZ

def titleToNumber(s):
    dic = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = dic.index(s[0]) + 1  # 取得H的索引下标
    for i in range(1, len(s)):
        result = 26*result + dic.index(s[i]) + 1
    return result

print(convertToTitle(234))
print(titleToNumber("HZ"))