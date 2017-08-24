# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 9:48'

import os
import mmap


with open('demo.bin', 'r+b') as f:
    print(f.fileno())  # 打印文件描述符
    m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
    print(type(m))
    print(m[0])
    m[4:8] = '\xff' * 4
