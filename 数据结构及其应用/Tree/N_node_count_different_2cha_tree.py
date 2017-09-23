# N个节点存在多少中不同的二叉树
def count(n):
    # root : 1
    # left : k
    # right : n-1-k
    if n == 0:  # 零个节点可以确定一个空树  ，递归出口
        return 1
    sum = 0
    for k in range(n):  # 循环[0, n-1]次
        sum += count(k) * count(n-1-k)  # 先乘法后求和
    return sum

print(count(1))  # 1
print(count(2))  # 2
print(count(3))  # 5
print(count(4))  # 14
print(count(5))  # 14
print(count(6))  # 大量的递归循环子问题，导致程序很慢
print(count(7))  # 大量的递归循环子问题，导致程序很慢
print(count(8))  # 大量的递归循环子问题，导致程序很慢
print(count(9))  # 大量的递归循环子问题，导致程序很慢
print(count(50))  # 大量的递归循环子问题，导致程序很慢


# # 优化后的程序,加上缓存
# # N 个节点存在多少中不同的二叉树
# def count(n):
#     # root : 1
#     # left : k
#     # right : n-1-k
#
#     if n == 0:  # 零个节点可以确定一个空树
#         return 1
#     sum = count.cache.get(n, 0)  # 在缓存中查找
#     if sum:  # 存在返回
#         return sum
#
#     for k in range(n):
#         sum += count(k) * count(n-1-k)  # 先乘法后求和
#         count.cache[n] = sum  # 将计算结果加入缓存中
#
#     return sum
# count.cache = {}  # 创建一个缓存，字典
# # count.cache = {0: 1}  # 创建一个缓存，初始化为，0个节点，能够造一种空树
# print(count(1))
# print(count(2))
# print(count(3))
# print(count(4))
# print(count(50))  # 大量的递归循环子问题，导致程序很慢1978261657756160653623774456
#

