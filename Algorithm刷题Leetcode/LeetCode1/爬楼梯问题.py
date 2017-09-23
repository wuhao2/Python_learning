# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 20:58'

"""
Climbing Stairs

这其实是一道组合数学的题目，总共有n步台阶，每次只能走一步或者两步，总共有多少种走法。
这个问题可以这样思考：假设已知有n步台阶共有f(n)种走法，对于n+1步台阶由两部分组成：
一个是前面n步台阶的f(n)种走法后直接一步到达n+1；
另一种是前面n-1步台阶的f(n-1)种走法后走两步到达n+1。因此可以得到递推关系是：f(n+1) = f(n) + f(n-1)。
"""
def climStairs(n):
    f = [1, 2]  # n=1,走法有f[0]=1种， n=2走法有f[1]=2,....., 台阶数为n时，走法为f[n-1]
    for i in range(2, n):
        f.append(f[i-2] + f[i-1])
    return f[n-1]

print(climStairs(10))