# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 15:14'

"""python2中"""
# quest = raw_input("what is you quest?")
# print(quest)

# python3中要达到python2的功能，可以使用eval函数
quest = eval(input("what is your quest?"))  # 输入必须是表达式
print(quest)

"""python3中"""
quest = input("what is your quest?")
print(quest)

