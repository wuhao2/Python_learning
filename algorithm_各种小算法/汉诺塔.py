# 汉诺塔问题
# a = [5, 4, 3, 2, 1], d = [],  c = []
# [],  [5], [ 4, 3, 2, 1]  # 这样就可以递归调用了
# [3, 2, 1], [5, 4], []
# 用三个栈来描述


def move(a, b, c, n):
    if n == 1:  # 递归出口
        # print('%s -> %s: %s' % (a[0], b[0], a[-1]))
        b.append(a.pop())
        # print(x, y, z)
        return
    move(a, c, b, n - 1)
    # print('%s -> %s: %s' % (a[0], b[0], a[-1]))
    b.append(a.pop())
    # print(x, y, z)
    move(c, b, a, n - 1)


# test
x = ['x:', 5, 4, 3, 2, 1]
y = ['y:']
z = ['z:']
move(x, y, z, 5)
print(x, y, z)
