# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/25 13:27'
keys = ["hello", "world", "love you"]
map(len, keys)    # calulate len(list)
zip(keys, map(len, keys))
print(list(zip(keys, map(len, keys))))
print(dict(zip(keys, map(len, keys))))