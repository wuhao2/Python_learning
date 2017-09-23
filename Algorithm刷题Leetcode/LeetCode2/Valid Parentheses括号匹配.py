# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/12 16:25'
left = {'(', '[', '{'}
right = {')', ']', '}'}

def ParenthesesMatch(express):
    s = []
    for c in express:
        if c in left:
            s.append(c)
        elif c in right:
            if s == []:
                return False  # 没有匹配成功
            if not  0<=ord(c) - ord(s[-1])<=2:
                return False

        s.pop()  # 匹配上了，出栈
    return True
print(ParenthesesMatch('[](){})'))  # True匹配
print(ParenthesesMatch('[]()){}'))  # Fause不匹配

