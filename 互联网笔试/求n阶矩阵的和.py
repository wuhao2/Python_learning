# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/26 15:56'

import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    ans = 0
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        for v in values:
            ans += v
    print(ans)



def maxSubArray(nums):
    l = g = -1000000000
    for n in nums:
        l = max(n, l + n)
        g = max(l, g)
    return g

