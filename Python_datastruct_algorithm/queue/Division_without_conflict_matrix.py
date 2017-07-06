from collections import deque
#划分动物函数
def division(M, n):
    cages = [] #用一个栈来存储所有的笼子
    q = deque(range(n))#初始化一个装满动物的队，队列
    previous = n#赋一个较大的数9，这样一开始就会创建笼子，用于存放动物

    while q:#当队列为空时，表示所有的动物都放进笼子了，不在循环了
        current = q.popleft()#从队头出队一个动物
        if previous >= current:#前一次的index大于当前的index，说明要创建新笼子了
            cages.append([])#创建新的笼子

        # 现在考察当前动物是否跟当前笼子中的动物是否右冲突
        for c in cages[-1]:#cages[-1]表示栈顶，也就是当前笼子，笼子里面有动物，可以用来迭代
            if M[current][c]:#当为1时，有冲突
                q.append(current)#放回队列尾部
                break
        else:#如果整个循环走完了，都没有break，说明当前动物跟当前笼子中的动物都没有冲突
            cages[-1].append(current)#将当前动物添加到当前笼子（栈顶笼子）
        previous = current#循环下一次的条件
    return cages#将笼子返回，笼子里面装了动物


N  = 9#9个动物
R = {#两两组合表示有冲突，动物会打架
    (1,4), (4,8), (1,8), (1,7),
    (8,3), (1,0), (0,5), (1,5),
    (3,4), (5,6), (5,2), (6,2), (6,4),
}
M= [[0]*N for _ in range(N)]#9*9的矩阵,0表示不冲突，1表示冲突
for i,j in R:
    M[i][j] = M[j][i] = 1#将R几何中的所有点都添加到矩阵当中，（1，4）和（4，1）表示一样的，都冲突
print("M:",M)

print("animal in cages: ",division(M,N))
