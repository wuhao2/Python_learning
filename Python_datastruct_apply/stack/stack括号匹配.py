# 输入一个表达式，看看括号是否匹配括号匹配
left = {'(', '[', '{'}
right = {')', ']', '}'}


def match(expr):
    s = []
    for c in expr:
        if c in left:
            s.append(c)
        elif c in right:
            if not s:  # 如果s为空
                return False
            if not 1 <= ord(c) - ord(s[-1]) <= 2:
                return False  # 不匹配
            s.pop()
    return not s  # 返回ture

print(match('[](){}'))  # True匹配
print(match('[]()){}'))  # Fause不匹配
