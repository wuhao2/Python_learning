# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 21:47'

"""
Reverse Integer

这个题是将一个整数逆序输出，当然如果是负数，符号不需要逆序。做法就是将其转化为字符串，然后逆序即可。
需要注意的陷阱就是当你逆序之后，该数可能超出了最大值2^31 - 1，需要做判断。
"""
def reverseInteger(x):
    if x >= 0:
        x = str(x)
        if int(x[::-1]) > (2**31-1):
            return 0
        else:
            return int(x[::-1])
    else:
        x = abs(x)
        x = str(x)
        if int(x[::-1]) > (2**31-1):
            return 0
        else:
            return int("-" + x[::-1])

print(reverseInteger(-123))