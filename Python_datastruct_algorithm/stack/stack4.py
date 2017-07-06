
#t为背包的总容量，w表示所有物品重量的一个列表
def knapsack(t, w):
    n = len(w)#可选的物品有n个
    s=[]#定义一个栈，当作一个背包
    k=0#用来表示物品的index

    #栈不为空或者有物品可选的时候循环
    while s or k<n:
        while t>0 and k<n:#背包容量大于零 并且k<n,进入循环
            if t >= w[k]:#如果t>后面的重量，才将索引入栈
                s.append(k)#index入栈
                t -= w[k]#背包空间减少了
            k+=1
        if t==0: #退出循环，找到了一组解
            print(s)

        k = s.pop()#回溯到index，即弹栈
        t+=w[k]#此时背包腾出了一个w[k]的空间
        k+=1#index向后索引

knapsack(10, [1,8,4,3,5,2])#得到下面的4组解
# [0, 2, 3, 5]
# [0, 2, 4]
# [1, 5]
# [3, 4, 5]