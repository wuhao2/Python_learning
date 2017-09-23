# _*_ coding: utf-8 _*_

"""
八皇后问题是一个以国际象棋为背景的问题：如何能够在 8×8 的国际象棋棋盘上放置八个皇后，
使得任何一个皇后都无法直接吃掉其他的皇后？为了达到此目的，任两个皇后都不能处于同一条横行、纵行或斜线上。
八皇后问题可以推广为更一般的n皇后摆放问题：
这时棋盘的大小变为n×n，而皇后个数也变成n。当且仅当 n = 1 或 n ≥ 4。

解题思路： 1、回溯法，逐行确定皇后所在列的位置  2、如果N行全部放完，则得到一个解
0  1  0  0
0  0  0  1
1  0  0  0
0  0  1  0

s = [1,3,0,2]得到一组解
s-->((0,1),(1,3)) 表示第0行的1， 第一行的3，这样就可以判断是否在同一斜线上
col表示下一次求解

for x,y in enumerate((1,4,5)):
    print(x,y)
# 0 1
# 1 4
# 2 5

"""
import random


def isValid(s, col):  # s = [1,3,0,2]得到一组解state；  col表示下一次求解
    row = len(s)  # 表示当前在哪一行

    for r, c in enumerate(s):  # 迭代每一行
        if c == col or abs(row - r) == abs(col - c):  # 不能在同一列，同一斜线
            return False

    return True


def queen(n, s=()):  # n*n的棋盘，每一个s都是一个半成品的解
    if len(s) == n:  # 递归出口
        return [s]

    res = []
    # s = (0)
    for col in range(n):  # 需要迭代n次，每个皇后必须要在不同的列
        if not isValid(s, col): continue  # 有冲突
        for r in queen(n, s + (col,)):  # ，迭代不同的行，每个皇后必须在不同的行； s+(col,)表示元组跟元组相加,把所有的解都添加到s元组中
            res.append(r)
    return res


# 测试,得到的所有解的列表
print([[(r, c) for r, c in enumerate(s)] for s in queen(8)])


# 冲突检查，在定义state时，采用state来标志每个皇后的位置，
# 其中索引用来表示横坐标，基对应的值表示纵坐标，例如： state[0]=3，表示该皇后位于第1行的第4列上
def conflict(state, nextX):
    nextY = len(state)  # 表示行
    for i in range(nextY):  # 迭代每一行
        # 如果下一个皇后的位置与当前的皇后位置相邻（包括上下，左右）或在同一对角线上，
        # 则说明有冲突，需要重新摆放
        if abs(state[i] - nextX) in (0, nextY - i):
            return True  # 有冲突
    return False  # 没冲突


# 采用生成器的方式来产生每一个皇后的位置，并用递归来实现下一个皇后的位置。
def queens(num, state=()):
    for pos in range(num):
        if not conflict(state, pos):
            # 产生当前皇后的位置信息
            if len(state) == num - 1:
                yield (pos,)
            # 否则，把当前皇后的位置信息，添加到状态列表里，并传递给下一皇后。
            else:
                for result in queens(num, state + (pos,)):
                    yield (pos,) + result


# 为了直观表现棋盘，用X表示每个皇后的位置
def prettyprint(solution):
    def line(pos, length=len(solution)):
        return '. ' * (pos) + 'X ' + '. ' * (length - pos - 1)

    for pos in solution:
        print(line(pos))


if __name__ == "__main__":
    # 得到了很多组解，随机抽取一组解
    prettyprint(random.choice(list(queens(8))))

"""
从序列中获取一个随机元素,随机取样
import random
print ("choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9]))
print ("choice('A String') : ", random.choice('A String'))

choice([1, 2, 3, 5, 9]) :  5
choice('A String') :  S

"""

"""
把函数变成constructor？ 在函数体里有yield就行了！
def gen():
    print ('enter')
    yield 1
    print ('next')
    yield 2
    print ('next again')
for i in gen():
    print (i)

# 各位！python看到gen函数里出现yield，知道可以用next了，问题是怎么对代码这个容器玩next？
# 从容器里拿到iterator的时候它还什么也不是，处在容器入口处，对于数组来说就是下标为-1的地方，对于函数来说就是函数入口嘛事没干，但是万事俱备就欠next。
# 开始for i in g，next让itreator爬行到yield语句存在的地方并返回值,
# 再次next就再爬到下一个yield语句存在的地方并返回值,依次这样直到函数返回(容器尽头)。
# yield的代码叠代能力不但能打断函数执行还能记下断点处的数据
"""
