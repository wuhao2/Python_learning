# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 9:36'
from random import randint

d = {x: randint(60, 100) for x in 'xyzabc'}

print(d)
print(d.keys())
print(d.values())  # return a list

print(sorted(d))  # sort by key
print(sorted(d.items(), key=lambda x: x[1]))  # sort by value
# [('y', 61), ('x', 66), ('c', 75), ('z', 80), ('b', 86), ('a', 97)]

tuple_data = zip(d.values(), d.keys())
# save memory space by using iterkeys and itervalues, but itervalues is delete in python3
# tuple_data1 = zip(d.itervalues(), d.iterkeys())
print(sorted(tuple_data))
# [(62, 'a'), (83, 'z'), (85, 'y'), (86, 'b'), (91, 'x'), (96, 'c')]
