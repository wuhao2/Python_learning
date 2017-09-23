# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/9 19:15'

def fibo(n):
    a, b = 0, 1
    res = []
    while b < n:
        res.append(b)

        # b = a + b
        # a = b

        a, b = b, a+b  # a+b 先计算a+b，但没有赋值，即运行完次指令后 a=1, b=1
    return res

print(fibo(100))

"""利用生成器求斐波那契"""
def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
print(list(fab(100)))


"""
输出一个平方与立方的表:
"""
# for x in range(1, 11):
#     print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
#     print(repr(x*x*x).rjust(4))
#
# for x in range(1, 11):
#     print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))


"""格式化输出"""
# table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
# for name, phone in table.items():
#     print('{0:10} ==> {1:10d}'.format(name, phone))
