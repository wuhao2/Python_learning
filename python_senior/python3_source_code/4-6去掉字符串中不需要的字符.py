# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 21:40'

"""
字符串替换
"""

s = '   abc   123   '
print(s.lstrip())  # 只去掉左端空白
print(s.rstrip())  # 只去掉右端空白
print(s.strip())   # 只去掉两端空白

print('&&&&&&'*10)
s1 = '+++sd::ff----'
print(s1.strip('+-'))  # sd::ff  去掉两边的---+++
print('&&&&&&'*10)
s2 = s1[:5] + s1[7:]  # +++sdff----切片加拼接，去掉了：：
print(s2)

print(s1.replace('+++', ''))  # sd::ff----
import re
print(re.sub('[+++----]', '', s1))  # sd::ff正则表达式

######################################################################
intab = "abcd"
outtab = "1234"
str_trantab = str.maketrans(intab, outtab)  # 做映射表
test_str = "csdn blog: http://blog.csdn.net/wirelessqa"  # 将其中的abcd分别替换成1234
print(test_str.translate(str_trantab)) # 3s4n 2log: http://2log.3s4n.net/wirelessq1

##################################################################
u = u'ní hǎo mā wǒ ài nǐ'
print(u)
print(u.translate(dict.fromkeys([])))