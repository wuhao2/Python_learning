# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 10:56'

"""
str转化成int：
1. 所有不能转换为字符串的都返回0
2. 出现多个+-号则不能转化，如++2不能转成2
3. 当所表示字符串大于2^31-1或小于-2^31时，返回2^31-1或小于-2^31
4. +-号后面必须接数字，否则返回0
5. " +0 123"应返回0，而不是123
"""
def atoi(str):
    if str == '':
        return 0
    str = list(str)
    result = []
    positive = negtive = 0  #
    has_digit = False
    for i in range(len(str)):
        if str[i] != '-' and str[i] != '+' and str[i].isdigit() == False and str[i] != ' ':
            if has_digit == False:
                return(0)
            else:
                break
        if str[i] == ' ' and has_digit:
            break
        if str[i] == ' ' and (negtive or positive):
            return 0
        if str[i] == '-':  # 如果str中存在+ -
            negtive += 1
        if str[i] == '+':
            positive += 1
        if negtive > 1 or positive > 1 or (negtive == 1 and positive == 1):  # 同时存在+-
            return 0
        if str[i].isdigit():  # 是数字
            has_digit = True
            result.append(str[i])

    result = ''.join(result)  # 转化为字符串
    if negtive:
        result = '-' + result
    if has_digit:
        if int(result) > 2**31 -1:  # 当所表示字符串大于2^31-1或小于-2^31时，返回2^31-1或小于-2^31
            return(2147483647)
        if int(result) < -2**31:
            return(-2**31)
        return(int(result))  # 字符串转化为整数
    else:
        return(0)

print(atoi("+72"))