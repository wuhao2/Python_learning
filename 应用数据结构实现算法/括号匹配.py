# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/23 20:37'

# 定义两个集合
Left = {'(', '[', '{'}
Right = {')', ']', '}'}

'''
输入一个括号表达式
匹配返回True，不匹配返回False
'''
def match(express):
    s = []
    for char in express:
        if char in Left:
            s.append(char)  # Left先压栈
        elif char in Right:
            if not s:  # s不是真的即栈为空
                return False
            # ord字符转化为ascii码
            if not 1 <= ord(char)-ord(s[-1]) <= 2:
                return False
            s.pop()
    else:
        return not s
        # 相当于问s是否为空， 为空返回true，不为空返回False

# test
print(match('(){}[]'))  # true 匹配
print(match('(){[}[]'))  # False 不匹配