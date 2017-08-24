# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 9:34'
f = open('demo.txt', 'w')

f.write('wefdsf')
f.write('wefdsf')
f.write('wefdsf')
f.write('wefdsf')
f.write('2143567')
f.write('\r\n')
f.write('wefdsf')
f.write('wefdsf')
f.write('2143567')
f.close()
# f1 = open('demo.txt', 'w', buffering=0)
# f2 = open('demo.txt', 'w', buffering=1)
# 全缓冲 : open函数的buffering设置大于1的整数n,n为缓冲区大小 linux默认为page的大小4096 满了n 个字节才会落盘
# 行缓冲 : open 函数的buffering设置为1 f=open(“demo.txt”,’w’,buffering=1) 碰到换行就会将缓冲区落盘
# 无缓冲 : open 函数的buffering设置为0 f=open(“demo.txt”,’w,’,buffering=0) 时时落盘到硬盘