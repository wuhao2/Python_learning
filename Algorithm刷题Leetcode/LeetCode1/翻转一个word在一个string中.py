# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 20:01'
"""
Reverse Words in a String

这个题的意思是，给定一个字符串，字符串是以单词的形式拼接起来的，需要做的就是把字符串里面的单词逆序输出，
但是单词内的顺序是不变的，相信看它的例子大家都能明白。这个题目用python里面的列表的话就非常简单，首先将字符串按“ ”分割，
然后去掉分割出来的列表中空格（因为两个单词间可能有多个空格，这是这个题目的陷阱），最后列表倒序再以空格拼接成字符串输出即可。代码如下：
"""

def reverseWords(s):
    tmp = s.split(' ')
    while '' in tmp:
        tmp.remove('')
    tmp.reverse()
    tmp = ' '.join(tmp)
    return tmp

s = 'ni hao wo ai'
print(reverseWords(s))