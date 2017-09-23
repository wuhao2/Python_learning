# 5*5的迷宫变成了7*7，是为了让每个点都有四条路可以走
def initMaze():
    maze = [[0]*7 for _ in range(5+2)]
    # 记录墙的位置
    walls = [
        (1, 3),
        (2, 1), (2, 5),
        (3, 3), (3, 4),
        (4, 2),  # (4,3),
        (5, 4),
    ]

    for i in range(5+2):
        maze[i][0] = maze[i][-1] = 1  # 第0列和最后一列都置1
        maze[0][i] = maze[-1][i] = 1  # 第0行和最后一行都置1
    # 将墙的位置都置1
    for i, j in walls:
        maze[i][j] = 1
    return maze


def path(maze, start, end):
    i, j = start  # 起始点和终点 元组拆包成坐标
    ei, ej = end
    # 创建一个栈，并且把起始点坐标入栈
    s = [(i, j)]
    maze[i][j] = 1  # 走过的点置1

    while s:  # 栈不为空，则进入while循环
        i, j = s[-1]  # 老鼠始终处于栈顶的位置

        if (i, j) == (ei, ej):  # 如果退回到起点时，退出while循环
            break
        for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:  # 上下左右四个方向走
            if maze[i+di][j+dj] == 0:
                maze[i + di][j + dj] = 1  # 置1
                s.append((i+di, j+dj))
                break  # 则退出for循环,返回到栈顶，走下一步，
        else:  # 没有遇到break，上下左右都不可走
            s.pop()  # 退回，栈为空，退出while循环，没有找到路径
    return s
maze = initMaze()
print("maze:", maze)
print("path:", path(maze, (1, 1), (5, 5)))