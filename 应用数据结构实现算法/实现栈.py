# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/24 10:08'

class Stack(object):
    def __init__(self, size):
        self.stack = []
        self.size = size
        self.top = -1

    def isFull(self):
        if self.size == self.top:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def push(self, content):
        if self.isFull():
            print("stack is full")
            return False
        else:
            self.stack.append(content)
            self.top += 1

    def pop(self):
        if self.isEmpty():
            print("stack is empty")
            return False
        else:
            self.stack.remove(self.stack[self.top])
            self.top -= 1

    def getStackData(self):
        return self.stack

    def getStackTopDate(self):
        return self.stack[self.top]

s = Stack(7)
s.push('wuhao')
s.push(32)
s.push(2.2)
s.push([99])

print("stack top pointer:", s.top)
print("stack list length:", len(s.stack))
print("current data of stack:", s.getStackData())
print("current data of stack:", s.getStackTopDate())
