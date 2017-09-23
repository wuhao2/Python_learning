from __future__ import with_statement
__author__ = 'wuhao'
__date__ = '2017/9/16 14:39'
import sys
import time
def test_encode_decode():
    shalom = '\u05dd\u05d5\u05dc\u05e9'
    text = shalom*1000000
    start = time.time()
    text_utf8 = text.encode('utf-8')
    text_utf16 = text.encode('utf-16')  # 编码
    assert text_utf8.decode() == text
    assert text_utf16.decode('utf-16') == text  # 解码
    end = time.time()-start
    print (end)
    return end

test = test_encode_decode
if __name__ == '__main__':
    times = [test() for i in range(10)]
    times.remove(max(times))
    times.remove(min(times))
    print('Average:', sum(times)/len(times))
# Python:3：Average: 0.035401612520217896
# Python2：('Average:', 0.43262505531311035)