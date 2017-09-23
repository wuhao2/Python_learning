# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/12 16:21'

def lengthOfLastWord(s):
    if s == '':
        return 0
    result = s.split()  # 默认以空格切分
    if result == []:
        return 0
    return len(result[-1])
print(lengthOfLastWord("ni hao wo ai nitto"))