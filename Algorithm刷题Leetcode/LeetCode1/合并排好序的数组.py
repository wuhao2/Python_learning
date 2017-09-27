# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/5 20:41'

"""
Merge Sorted Array

这个题目的意思是把两个排好序的序列合并为一个排好序的序列，本来我最开始想的是直接把两个序列拼接在一起，
然后用python列表里面自带的sort函数排个序就Ok了，但是这样做的复杂度至少是O((m+n)log(m+n))的，
另外一种O(m+n)做法是从后面往前面排，比如合并后的最后一个数A[m+n-1]就应该等于A[m-1]和B[n-1]中较大的一个以此类推，
这样可以避免从前往后需要移动的操作，需要注意的特列就是A和B中某一个为空
"""

def merge(A, m, B, n):
    '''

    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    '''
    def merge(A, m, B, n):
        for i in range(m+n-1, -1, -1):
            if m == 0 or (n > 0 and B[n-1] > A[m-1]):  # 判断A、B是否为空
                A[i] = B[n-1]
                n -= 1
            else:
                A[i] = A[m-1]
                m -= 1
        return A
A = [2, 3, 4]
B = [3, 5, 7]
print(merge(A, 3, B, 3))