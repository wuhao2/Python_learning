# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 9:11'

import struct
f = open('demo.wav', 'rb')
info = f.read(44)

struct.unpack('h', info[22:24])  # voice channels 小端解析任意数据类型的数据

import array
# f.seek(0, 2)
# f.tell()
n = int((f.tell() - 44)/2)  # 数组的长度
buf = array.array('h', (0 for _ in range(n)))
f.seek(44)
f.readinto(buf)  # 把数据读入buf中

for i in range(n):  # 采样缩小，使得声音变小
    buf[i] /= 8

with open('demo2.wav', 'wb') as f2:
    f2.write(info)
    buf.tofile(f2)
