from collections import deque  # 线程安全
# 属于状态空间图的广度优先搜索问题，


def a_to_b(a, b):
    q = deque([(a, 0)])  # 初始化一个队列，存放一个元组（状态值，记录操作数）
    checked = {a}  # 定义一个集合，用来存储已经检查过的状态值

    while True:
        status, count = q.popleft()  # 出队列的是一个元组，拆包成 状态和记录操作数
        if status == b:
            break
        q.append((status + 1, count + 1))  # 将变化的状态入队列
        q.append((status * 2, count + 1))
        q.append((status - 1, count + 1))

        # 可以优化为：
        # 如果status已经大于b了，+1和*2这两种状态，就没有必要在入队列了，只会越来越大
        if status < b:
            if status+1 not in checked:  # 消除checked集合中的重复状态值，避免重复入队列
                q.append((status+1, count+1))
                checked.add(status+1)
            if status*2 not in checked:
                q.append((status*2, count+1))
                checked.add(status*2)
        # # 如果status小于0了，就没有必要在入队列了，只会越来越小
        if status > 0:
            if status-1 not in checked:
                q.append((status - 1, count + 1))
                checked.add(status-1)
    return count

print("操作次数:", a_to_b(5, 8))
print("操作次数:", a_to_b(3, 11))
print("操作次数:", a_to_b(24, 246))