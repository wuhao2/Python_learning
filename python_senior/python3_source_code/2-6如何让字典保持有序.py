# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 10:41'

# d ={} # 默认字典
# d['Jim'] = (1, 35)
# d['Leo'] = (2, 37)
# d['Bob'] = (3, 41)
# for k in d:
#     print(k)  # 不是有序的遍历
# # Leo
# # Jim
# # Bob

# from collections import OrderedDict
# d1 = OrderedDict()  #有序字典
# d1['Jim'] = (1, 35)
# d1['Leo'] = (2, 37)
# d1['Bob'] = (3, 41)
# for k in d1:
#     print(k)  # 有序的遍历，先进先遍历
# # Jim
# # Leo
# # Bob

###########################################################
from time import time
from random import randint
from collections import OrderedDict
player = list('ABCDEFGH')
start = time()
d = OrderedDict()
for i in range(8):
    input()
    p = player.pop(randint(0, 7-i))
    end = time()
    print(i+1,  p,   end-start)
    d[p] = (i+1, end-start)

print()
print("*"*20)
for k in d:
    print(k,  d[k])  # 打印键和值


"""
int(x [,base])
将x转换为一个整数

float(x)
将x转换到一个浮点数

complex(real [,imag])
创建一个复数

str(x)
将对象 x 转换为字符串

repr(x)
将对象 x 转换为表达式字符串

eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象

tuple(s)
将序列 s 转换为一个元组

list(s)
将序列 s 转换为一个列表

set(s)
转换为可变集合

dict(d)
创建一个字典。d 必须是一个序列 (key,value)元组。

frozenset(s)
转换为不可变集合

chr(x)
将一个整数转换为一个字符

unichr(x)
将一个整数转换为Unicode字符

ord(x)
将一个字符转换为它的整数值

hex(x)
将一个整数转换为一个十六进制字符串

oct(x)
将一个整数转换为一个八进制字符串



"""