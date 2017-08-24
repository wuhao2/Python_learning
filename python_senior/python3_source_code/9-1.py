# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/19 13:59'

# 改进版2：
"""
装饰器函数
"""
def memo(func):
    cache = {}
    def wrap(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrap
"""
斐波那契数列：1 1 2 3 5 8 13........
重复计算子问题
"""
@memo  # 语法糖，等价于 fibonacci = memo(fibonacci)
def fibonacci(n):
    if n <= 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
# fibonacci = memo(fibonacci)  # 装饰器函数添加之后，悄悄的改变了函数的功能
print(fibonacci(50))  # 计算很慢，因为要重复计算太多的子问题


"""
==>一个共有n个台阶的楼梯，从下面走到上面，
一次只能迈1，2，3个台阶
==>  并且不能后退，走完这个楼梯共有多少中方法（典型回溯法问题）
"""
@memo  # 等价 climb = memo(climb)
def climb(n, steps):
    count = 0
    if n == 0:
        count = 1
    elif n > 0:
        for step in steps:
            count += climb(n-step, steps)
            # 假设第一次走了1一个台阶，那么剩下的n-1个台阶，继续走
    return count
# climb = memo(climb)
print(climb(20, (1, 2, 3)))  # 悄悄的改变了函数的功能得到：121415



###########################################################
# 改进版1：直接改动没有使用装饰器函数
def fibonacci2(n, cache=None):
    if cache is None:
        cache = {}  # 创建缓存
    if n in cache:
        return cache[n]  # 每次去缓存中取得，如果有并返回
    if n <= 1:
        return 1
    # 如果缓存中没有，则去计算
    cache[n] = fibonacci2(n - 1, cache) + fibonacci2(n - 2, cache)
    return cache[n]
    # print(fibonacci2(50))  # 计算很快，得到20365011074