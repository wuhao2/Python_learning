#栈的实现,是一个容器，和列表不同的是，栈只能操作栈顶的数据，先进后出;
# 而列表中的任意元素都可以被操作

class Stack (object):
    #初始化self表示栈的主体
    def __init__(self, size):
        self.stack = []#列表也是一个容器,也是栈的最基础形式
        self.size = size#栈的容量
        self.top = -1#栈顶指针，最初的时候，栈顶和栈底是重合的，当有数据进来的时候，栈顶指针加1
    #入栈
    def push (self, content):
        if self.isfull():
            print("stack is full")
        else:
            self.stack.append(content)
            self.top = self.top +  1
    #出栈
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            self.stack.remove(self.stack[self.top])
            self.top = self.top - 1

    # 获得当前栈中的数据
    def getStackData(self):
        return self.stack

    def isfull(self):
        if self.top == self.size:
            return True
        else:
            return False
    def isempty(self):
        if self.top == -1:
            return True
        else:
            return False


a = Stack(7)
print("stack top pointer:",a.top)
print("stack is empty or not:",a.isempty())
print("stack size:",a.size)

print("入栈***********")
str = 'wuhao'
int = 222
a.push(str)
a.push(int)
print("stack top pointer:",a.top)
print("stack list length:",len(a.stack))
print("current data of stack:", a.getStackData())


print("出栈***********")
x = a.pop()
print("stack top pointer:",a.top)
print("stack list length:",len(a.stack))
print("出栈的内容：",x)
print("current data of stack:", a.getStackData())
