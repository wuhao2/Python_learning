# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 20:13'
"""
Single Number

这个题和下一个题都很有技巧，这个题的意思是给定一个序列，这个序列中的数除了有一个数只出现过一次外，
其他的数都出现两次，请找出这个只出现一次的数。最直观的想法就是遍历一遍把每个数出现的次数都存起来，
然后再看谁的次数为1。但是网上有一种更加简洁而巧妙地方法，用异或来解决这个问题，
他的思想是两个相同的数异或为0,0和任何数异或为任何数，
这样只需要把整个序列全都异或一遍，最后得到的数就是想要的答案了。
"""


def singleNumber(A):
    res = 0
    for i in A:
        res = res ^ i
    # 相同元素异或为0, 0与任何数异或等于任何数， 有a^b^a = b
    # 此外，异或还可以用于两个元素交换a = a^b^(b=a)
    return res


A = [1, 3, 4, 4, 2, 2, 1]
print(singleNumber(A))

"""
Single Number II

这个题更加巧妙，题目与上一个题目类似，不过这一次序列中的数字除了某一个数字外都出现3次，
需要找出这个数字，先贴代码再解释。
"""


def singleNumber2(B):
    ones, twos = 0, 0
    for ele in A:
        ones = ones ^ ele & ~twos
        twos = twos ^ ele & ~ones
    return (ones)


B = [1, 2, 3, 4, 4, 2, 4, 3, 3, 1]
print(singleNumber2(B))