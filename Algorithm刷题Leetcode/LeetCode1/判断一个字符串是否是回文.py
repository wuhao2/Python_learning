# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 20:32'
"""
Valid Palindrome

这个题是判断一个字符串是否是回文，回文的意思是正序和逆序都一样，所以这也成了我们判断的标准，
这个题的回文是不区分大小写的，因此首先可以将所有字母转为小（大）写，需要注意的是它这里只关注字母和数字，
因此其他的符号需要去掉，需要用到了python的正则表达式。
"""
import re
def isPalindrome(s):
    s = s.lower()  # 首先将字符串转为小写
    s = re.sub('[^A-Za-z0-9]', '', s)  # 正则表达式去除非字母和数字的符号
    if s == s[::-1]:
        return True
    else:
        return False

s = '123321'
print(isPalindrome(s))  # 返回ture