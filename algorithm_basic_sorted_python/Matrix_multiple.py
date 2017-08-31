# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/9 15:06'
def matrixMul(A, B):
    res = [[0] * len(B[0]) for i in range(len(A))]  # 得到 res矩阵的维度：A矩阵的行 * B矩阵的列
    for i in range(len(A)):  # A矩阵的行数
        for j in range(len(B[0])):  # B矩阵列数
            for k in range(len(B)):  # B矩阵的行数
                res[i][j] += A[i][k] * B[k][j]
    return res

def matrixMul2(A, B):
    return [[sum(a * b for a, b in zip(a, b)) for b in zip(*B)] for a in A]

a = [[1, 2], [3, 4], [5, 6], [7, 8]]
b = [[1, 2, 3, 4], [5, 6, 7, 8]]

print(matrixMul(a, b))
print(matrixMul(b, a))
print("-"*90)

# print(matrixMul2(a, b))
# print(matrixMul2(b, a))
# print("-"*90)


# from numpy import dot
# print(map(list, dot(a, b)))
# print(map(list, dot(b, a)))




"""
# 求矩阵的转置
"""
matrix = [
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [1, 2, 3, 4],
]
# way 1
# transpose = [[row[i] for row in matrix] for i in range(4)]
# print(transpose)

# way 2
# transpose = []
# for i in range(len(matrix[0])):
#     transpose.append([row[i] for row in matrix])
# print(transpose)

# way 3
# transposed = []
# for i in range(len(matrix[0])):
#     transposed_row = []  # 转置矩阵的行
#     for row in matrix:
#         transposed_row.append(row[i])
#     transposed.append(transposed_row)
# print(transposed)