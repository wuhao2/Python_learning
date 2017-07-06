from  collections import deque
#杨辉三角的每一层，都是二项式的系数
def yanghui(k):
    #0-->1--->2....-->k
    q = deque([1])#第一层队列中只有一个1
    for i in range(k):#表示每一层都要进行出队列
        for _ in range(i):#表示每一层都要出队列i次，即第几层就出队列几次
            q.append(q.popleft() + q[0])#加上q[0]的意思就是说加上出队列后的队列中的第一个元素
        q.append(1)

    return list(q)
#测试
print(yanghui(1))
print(yanghui(2))
print(yanghui(3))
print(yanghui(4))



