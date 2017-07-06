# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 15:38 '
"""
1.问题描述:
某古寺的一块石碑上依稀刻有一些神秘的自然数。
专家研究发现：这些数是由1,3,5,7,9这5个奇数字排列组成的5位素数，
同时去掉它的最高位与最低位数字后的3位数还是素数，同时去掉它的高二位与低二位数字后的一位数还是素数。
因此人们把这些神秘的素数称为金蝉素数，喻意金蝉脱壳之后仍为美丽的金蝉。

试求出石碑上的金蝉素数。
"""
#解题思路：
# 1. 生成 1,3,5,7,9 全排列, 每种排列是一个元组
# 2. 元组转换成数字 (例: 13579,357,159)
# 3. 检测3个数字是素数，如全是素数则是金蝉数

import math
def isPrimeNum(n):
    for k in range(2, int(math.sqrt(n) + 1)):#素数是不能被因式分解的数，除了1和本身
        if n % k == 0:#如过一个数n， n/sqrt(n) != 0 则这个数是素数
            return False
    return True
#test
print(isPrimeNum(41))

from itertools import permutations
from functools import reduce
for p in permutations([1,3,5,7,9], 5):#列表中的5个数进行排列组合
    # (3,5,7), (1,5,9), (1,3,5,7,9)
    for l in (p[1:-1], p[::2], p):
        s = reduce(lambda x, y: 10 * x + y, l)
        if not isPrimeNum(s):
            break
    else:
        print (p)

# (1, 3, 5, 9, 7)
# (1, 5, 9, 3, 7)
# (5, 1, 9, 7, 3)
# (5, 3, 7, 9, 1)
# (7, 9, 5, 3, 1)
# (9, 1, 5, 7, 3)