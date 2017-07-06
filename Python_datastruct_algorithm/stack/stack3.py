
#后缀表达式的求值
operators = {
    '+': lambda op1,op2: op1+op2,
    '-': lambda op1,op2: op1-op2,
    '*': lambda op1,op2: op1*op2,
    '/': lambda op1,op2: op1/op2,
}

def evalPstfix(e):#传入一个表达式
    tokens = e.split()#按空格切分成字符串列表
    s = []#定义个栈

    for token in tokens:
        if token.isdigit():#token是数字就压栈
            s.append(int(token))#token是字符串，要先转换为int
        elif token in operators:#如果是操作符
            f = operators[token]#从字典中拿出这个操作符
            op2 = s.pop()
            op1 = s.pop()
            s.append(f(op1,op2))
    return s.pop()
#测试
print (evalPstfix('2 3 4 * +'))#14



