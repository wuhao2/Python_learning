# 比赛统计分数
import random


# random.randint(0,100)包含后端点
def averageScore(n):
    s = []
    for i in range(n):
        s.append(random.randint(0, 100))  # 每产生一个0-100的随机数，就放入列表中
    maxScore = 0
    minScore = 100
    sumScore = 0

    for j in s:
        if maxScore < j:
            maxScore = j
        if minScore > j:
            minScore = j
        sumScore += j
    averageScore = (sumScore - minScore - maxScore) / (n - 2)  # 效率不高

    print(s, maxScore, minScore, averageScore)


def averageScore1(n):
    s = [random.randint(0, 100) for i in range(n)]
    print(s, sum(s), min(s), max(s))
    return (sum(s) - max(s) - min(s)) / (n - 2)  # 效率很高，内置函数底层是用C语言


averageScore(10)
print(averageScore1(10))
