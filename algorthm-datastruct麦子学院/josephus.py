# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/7 16:47'

'''
题目：0，1，...，n-1这n个数字排成一个圆圈，从数字0开始每次从这个圆圈里删除第m个数字。
求出这个圆圈里剩下的最后一个数字。
'''


def josephus(n, m):
    if type(n) != type(1) or n <= 0:
        raise Exception('n must be an integer(n > 0)')
    if n == 1:
        return 0
    else:
        return (josephus(n - 1, m) + m) % n


if __name__ == '__main__':
    print(josephus(4, 3))


