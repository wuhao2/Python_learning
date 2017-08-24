# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 9:15'
# way1：
from random import randint
list = [randint(0, 20) for _ in range(20)]
c = dict.fromkeys(list, 0)
for x in list:
    c[x] += 1
print(c)

# way:2：
from collections import Counter
c2 = Counter(list)
print(c2.most_common(3))

# way3：
import re
txt = open('word.txt').read()
word_count = re.split('\W+', txt)  #
print(word_count)
Counter(word_count)
