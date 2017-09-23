# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 16:07'

# f = open("foo.txt", "wb")
# f.write("Hello world/n")  # python3中error

f = open("foo.txt", "w")
f.write("Hello world/n")  # python3中已str方式写文件

f = open("foo.txt", "wb")
f.write(b"Hello world")  # python3中以二进制方式写文件

f = open("foo.txt", "w", encoding='ASCII')
f.write("Hello world")  # python3中以assic编码写文件
