# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 15:41 '

# 队列的实现
class Queue():
    def __init__(qu, size):
        qu.queue = []
        qu.size = size
        qu.head = -1
        qu.tail = -1

    def Empty(qu):
        if qu.head == qu.tail:
            return True
        else:
            return False

    def Full(qu):
        if qu.tail - qu.head == qu.size:
            return True
        else:
            return False
    #入队列
    def enQueue(qu, content):
        if qu.Full():
            print ("Queue is Full!")
        else:
            qu.queue.append(content)
            qu.tail = qu.tail + 1
    #出队列
    def outQueue(qu):
        if qu.Empty():
            print("Queue is Empty!")
        else:
            qu.queue.remove(qu.queue[qu.head])
            qu.head = qu.head + 1
    #输出队列中的内容
    def getQueueData(self):
        return self.queue

q = Queue(7)
print("queue is empty or not:", q.Empty())
print("********************入队列之后**********************")
q.enQueue("wuhao")
q.enQueue("wushibing")
q.enQueue(5)
q.enQueue(8)
print(q.getQueueData())
print("********************出队列之后**********************")
q.outQueue()
q.outQueue()
print(q.getQueueData())

