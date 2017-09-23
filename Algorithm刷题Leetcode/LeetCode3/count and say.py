# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 8:50'

"""
这个题有点不好理解，反正我是看了网上的意思才懂了，意思是比如从1开始，因为只有1个1，
所以第二个数就是11（表示1个1），第二个数有2个1，所以第三个数为21（表示2个1），
第三个数有1个2,1个1，所以第四个数是（1211）以此类推，懂了意思就好做了。
"""
def countAndSay(n):
    if n == 1:
        return '1'
    if n == 2:
        return '11'
    # result = []
    s = '11'
    for i in range(n - 2):
        s = Trans(s)
    result = ''.join(s)
    return result

def Trans(s):
    result = []
    tmp, count = s[0], 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
            if i == len(s) - 1:
                result.append(str(count) + s[i - 1])
        else:
            result.append(str(count) + s[i - 1])
            tmp, count = s[i], 1
            if i == len(s) - 1:
                result.append(str(count) + s[i])
    result = ''.join(result)
    return result

print(countAndSay(11))