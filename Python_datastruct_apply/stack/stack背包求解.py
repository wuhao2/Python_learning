# total为背包的总容量，weight_list表示所有物品重量的一个列表
def knapsack(total, weight_list):
    count = len(weight_list)  # 可选的物品有n个
    stack_snap = []  # 定义一个栈，当作一个背包
    index = 0  # 用来表示物品的index

    # 栈不为空或者有物品可选的时候循环
    while stack_snap or index < count:
        while total > 0 and index < count:  # 背包容量大于零 并且index<count,进入循环
            if total >= weight_list[index]:  # 如果total>后面的重量，才将索引入栈
                stack_snap.append(index)  # index入栈
                total -= weight_list[index]  # 背包空间减少了
            index += 1
        if total == 0:   # 退出循环，找到了一组解
            print(stack_snap)

        # 回溯
        index = stack_snap.pop()  # 回溯到index，即弹栈
        total += weight_list[index]  # 此时背包腾出了一个w[k]的空间
        index += 1  # index向后索引

knapsack(10, [1, 8, 4, 3, 5, 2])  # 得到下面的4组解
# [0, 2, 3, 5]
# [0, 2, 4]
# [1, 5]
# [3, 4, 5]