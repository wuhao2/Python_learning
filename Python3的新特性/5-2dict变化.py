# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 15:53'

d = {1: "dead", 2: "parrot"}
print(d.items())  # 返回了可迭代对象字典
for values in d.items():
    print(values)
keys = list(d.keys())
print(keys)
values = list(d.values())
print(values)
