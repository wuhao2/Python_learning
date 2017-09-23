# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 11:46'
x = [1, 2, 3]
y = [4, 5]
# x.append(y)
# print(x)
x.extend(y)
print(x)
items = [1, 2]
if items == []:
    print("空列表")
if len(items) == 0:
    print("空列表")
if not items:     # 判断一个list是否为空，最优雅的方式
    print("空列表")

# 如何拷贝一个列表对象
import copy
old_list = [1, 3]
# 浅拷贝
new_list = copy.copy(old_list)
# 深拷贝
new_list = copy.deepcopy(old_list)

item = [{'name': 'Homer', 'age': 39},
         {'name': 'Bart', 'age': 10},
         {"name": 'cater', 'age': 20}]

item.sort(key=lambda item: item.get("age"))
print(item)
# new_items = sorted(items, key=lambda item: item.get("age"))  # 得到新的列表
# print(new_items)