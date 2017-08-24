# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/24 9:14'

operators = {
    "+": lambda op1, op2: op1+op2,
    "-": lambda op1, op2: op1-op2,
    "*": lambda op1, op2: op1*op2,
    "/": lambda op1, op2: op1+op2
}


def evaluate_profix_expr(expr):
    string = expr.split()
    s = []
    for token in string:
        if token.isdigit():
            s.append(int(token))
        elif token in operators:
            f = operators[token]
            op1 = s.pop()
            op2 = s.pop()

            s.append(f(op1, op2))
    return s
# 测试
print(evaluate_profix_expr('2 3 4 * +'))  # 14