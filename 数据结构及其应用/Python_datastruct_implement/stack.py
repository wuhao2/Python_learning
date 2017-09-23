# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 15:40 '


# Python的扩展数据结构
# 栈的实现
class Stack(object):
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    # 入栈
    def push(self, content):
        if self.Full():
            print("Stack is Full!")
        else:
            self.stack.append(content)
            self.top += 1

    # 出栈
    def out(self):
        if self.Empty():
            print("Stack is Empty!")
        else:
            self.stack.remove(self.stack[self.top])
            self.top -= 1

    def Full(self):
        if self.top == self.size:
            return True
        else:
            return False

    def Empty(self):
        if self.top == -1:
            return True
        else:
            return False


s = Stack(7)
s.push("wuhao")
s.push("wushibing")
s.push("niluo")
s.push("daijiali")
s.out()
print("容量: ", s.size)
print("栈顶指针: ", s.top)
print("栈中的数据是：", s.stack)
print("栈顶元素是：", s.stack[-1])
