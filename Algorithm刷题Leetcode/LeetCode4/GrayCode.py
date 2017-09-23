# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/17 15:02'
"""
输出格雷码的十进制数，包括两步，第一步是给出格雷码，第二步是将二进制转成十进制的数。
难点是格雷码的转换，但是知道他的规则就好做了，规则如下：
1. 位格雷码有两个码字
2. (n+1)位格雷码中的前2n个码字等于n位格雷码的码字，按顺序书写，加前缀0
3. (n+1)位格雷码中的后2n个码字等于n位格雷码的码字，按逆序书写，加前缀1
有了以上规则就简单了，代码如下：
"""
def grayCode(n):
    tmp = ['0', '1']
    if n == 0:
        return [0]
    if n == 1:
        return convert2integer(tmp)
    result = []
    for i in range(n - 1):
        for j in tmp:
            result.append('0' + j)
        for j in tmp[::-1]:
            result.append('1' + j)
        tmp = result
        result = []
    return convert2integer(tmp)

def convert2integer(tmp):
    tt = []
    for i in tmp:
        result = int(i[0])
        for j in range(1, len(i)):
            result = 2*result + int(i[j])
        tt.append(result)
    return tt

# test
print(grayCode(1))
print(grayCode(2))
print(grayCode(3))
print(grayCode(4))