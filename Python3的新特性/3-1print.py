# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 14:55'

# python2中的<>  被 ！= 代替
# int(214) 、long(33333333333L) -------》 int

"""python3"""
fid = open("log.txt", 'w')
print("log.txt", file=fid)
print("hello")

"""python2"""
# fid = open("log.txt", 'w')
# print>>fid, "log text"  # 重定位到log.txt
# print "hello"

"""python3"""
print("Foo", "Bar", sep="%")  # 链接两个字符串，连接符为%
