from __future__ import with_statement

# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 18:10'
import sys
import time
import json


def test_json():
    x = dict(a=1, b='BBBB', c=4.56)
    x6 = 6 * [x]
    y = dict(z=x6, zz=2 * x6, zzz=3 * x6)
    print(y)
    o = 100 * [y]
    start = time.time()
    j = json.dumps(o)
    assert json.loads(j) == o
    end = time.time() - start
    return end


test = test_json
if __name__ == '__main__':
    times = [test() for i in range(10)]
    times.remove(max(times))
    times.remove(min(times))
    print('Average:', sum(times) / len(times))
    # json模块的C扩展，效率得到了很大的提升，