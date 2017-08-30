# 队列的实现，队列是单向的，数据从队尾进队首出
# 如果一端只进行插入操作，则为队尾；如果一端只进行删除操作，则叫队首


class Queue():
    def __init__(self, size):
        self.queue = []
        self.size = size
        self.head = -1
        self.tail = -1

    def isempty(self):
        if self.head == self.tail:  # 头指针等于尾指针
            return True
        else:
            return False

    def isfull(self):
        if self.tail - self.head == self.size:
            return True
        else:
            return False

    # 入队列
    def enter_queue(self, content):
        if self.isfull():
            print("queue is full")
        else:
            self.queue.append(content)
            self.tail += 1  # 每次入队，队尾指针加1

    # 出队列
    def out_queue(self):
        if self.isempty():
            print("queue is empty")
        else:
            self.queue.remove(self.queue[0])
            self.head += 1  # 每次出队，队首指针加1，队尾指针不变

    # 获取当前队列中的内容
    def getQueueData(self):
        return self.queue

q = Queue(4)
print(q.size)
print(q.head, q.tail)
print(q.isempty())
print(q.isempty())


q.enter_queue("python")
print(q.head,q.tail)
q.enter_queue("java")
print(q.head,q.tail)
q.enter_queue("C/C++")
print(q.head,q.tail)
q.enter_queue("JS")
print(q.head,q.tail)
print(q.getQueueData())

# q.out_queue()
# print(q.head,q.tail)
q.out_queue()
print(q.head, q.tail)
q.out_queue()
print(q.head, q.tail)
print(q.getQueueData())





