# 有4个砝码,总重量是40g. 砝码的质量是整数,且各不相等.
# 请确定她们的质量,使之能称出1-40g任何整数质量的物体

# r(1): 1 一个砝码只能表示1
# r(1，3）：1，2，3，4 两个砝码能够表示1，2，3，4
# r(1，3， 5）：1，2，3，4, 5, 6, 7, 8, 9 两个砝码能够表示1，2，3，4, 5, 6, 7, 8, 9

# r(1, 3, k): k-4--- k+4


def fun(max, n):
    """
    :param m: 砝码表示的重量范围最大值
    :param n: 砝码的个数
    :return: 返回一个装满4个砝码的列表
    """
    res = []
    while n > 1:
        k = sum(res) * 2 + 1  # 根据分析，砝码的重量应该满足这个公式
        res.append(k)
        n -= 1
    k = max - sum(res)  # 得到最后一个数
    if k - sum(res) - sum(res) < 2:
        res.append(k)
        return res
    return None


print(fun(40, 4))  # [1, 3, 9, 27]




# for a in range(10):
#     for b in range(10):
#         if a == b: continue
#         for c in range(10):
#             if a==c or b == c: continue
#             for d in range(10):
#                 if d==a or d==b or d==c: continue
#                 s = a + b + c + d
#                 if s in [range(1,11)]:
#                     print(a, b, c,d)
