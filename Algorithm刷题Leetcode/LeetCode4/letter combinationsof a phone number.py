# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 13:35'


def letterCombinations(digits):
    if digits == '':
        return ['']
    dic = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}
    for i in range(len(digits)):
        if digits[i] == '1' or digits[i] == '0':
            continue
        digits = digits[i:len(digits)]
        break
    result = dic[digits[0]]
    for i in range(1, len(digits)):
        if digits[i] == '1' or digits[i] == '0':
            continue
        tmp1 = []
        for j in range(len(result)):
            for k in range(len(dic[digits[i]])):
                tmp1.append(result[j] + dic[digits[i]][k])
        result = tmp1
    return result

print(letterCombinations('234'))
