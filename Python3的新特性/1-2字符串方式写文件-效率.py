from __future__ import with_statement
# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 14:29'
import sys
import time
c = 'X'

def test_write_speed():
    start = time.time()
    with open('1-2.txt', 'w') as f:  # 以字符串方式写文件
        for i in range(5000000):
            f.write(c)
    end = time.time()-start
    print(end)
    return end

times = [test_write_speed() for i in range(10)]
times.remove(max(times))
times.remove(min(times))
print('Average:', sum(times)/len(times))  # 平均用时Average: 2.1528933942317963
