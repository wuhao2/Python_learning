# _*_ coding: utf-8 _*_  # python3默认是Unicode编码，所以不需要coding=utf-8
from __future__ import with_statement
__author__ = 'wuhao'
__date__ = '2017/9/16 14:19'

import sys
import time
if sys.version_info[0] == 3:
    exec("c = b'X'")  # 字节
else:
    c = 'X'  # 字符串

def test_write_speed():
    start = time.time()
    with open('1.txt', 'wb') as f:  # 以字节方式写文件
        for i in range(5000000):
            f.write(c)
    end = time.time()-start
    print(end)
    return end

times = [test_write_speed() for i in range(10)]
times.remove(max(times))  # 去掉一个最大值
times.remove(min(times))  # # 去掉一个最小值
print('Average:', sum(times)/len(times))  # Python3中取平均值Average: 0.9897673428058624
# Python2中('Average:', 1.798499971628189)