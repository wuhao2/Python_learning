# _*_ coding: utf-8 _*_

__author__ = 'wuhao'
__date__ = '2017/7/25 13:00'

mylist = [0, 1, 3, -1]

print(all(map(lambda x: x > 0, mylist)))
print(any(map(lambda x: x > 0, mylist)))

if all(map(lambda x: x > 0, mylist)):
    print("all items are greater than 0")
if any(map(lambda x: x > 0, mylist)):
    print("at least one item is greater than 0")
