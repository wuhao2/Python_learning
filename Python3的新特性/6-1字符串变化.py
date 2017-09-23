# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 15:57'

césar = ["author", "consultant"]
print(césar)   # python3中默认为unicode编码，
print(repr('é'))  # 转换为unicode码， 而python2中转换成ASSIC码

b = b'china'
print(type(b))  # 新类型，字节类型<class 'bytes'>

s = b.decode()  # Byte--转化为->str
print(s)  # china
b1 = s.encode()  # str--转化为-->Byte
print(b1)  # b'china'
