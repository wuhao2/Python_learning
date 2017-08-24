# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/15 12:38'

"""
# for迭代
data = [2, 4, -3, 4, 0]
for i in data:
    if i < 0:
        print(data[i])

# 过滤函数
from random import randint
data = [randint(-10, 10) for _ in range(10)]
print(data)
filter_data = filter(lambda x: x >= 0, data)
print(filter_data)

# 列表解析
list_parse_data = [x for x in data if x >= 0]
print(list_parse_data)
"""



import timeit  # 测试Python表达式的运行时间
# print(timeit.timeit([x for x in data if x >= 0]))
# print(timeit.timeit(filter(lambda x: x >= 0, data)))
# print(timeit.timeit('"-".join(map(str, range(1000)))', number=10000))   # 2.142661982286215

"""
# 字典代与字典解析迭
d = {x: randint(0, 100) for x in range(1, 21)}
print(d)

dict_iter_value = {k for k in d.values()if k > 15}
dict_iter_key = {k for k in d.keys()if k > 15}

print(dict_iter_value)
print(dict_iter_key)

dict_parse = {k: v for k, v in d.items() if v > 90}  # 同时迭代键和值
print(dict_parse)
"""

# 集合
from random import randint
s = {randint(-10, 10) for _ in range(10)}
print(s)
set_parse = {x for x in s if x%3 == 0}
print(set_parse)
