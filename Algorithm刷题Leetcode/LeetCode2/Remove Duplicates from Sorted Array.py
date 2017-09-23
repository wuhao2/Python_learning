# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/12 14:30'


def removeDuplicates(A):
    if A == []:
        return 0
    count = 1
    for i in range(1, len(A)):
        if A[i] != A[i - 1]:
            A[count] = A[i]
            count += 1
    return count, A


A = [1, 1, 2, 3]
print(removeDuplicates(A))
