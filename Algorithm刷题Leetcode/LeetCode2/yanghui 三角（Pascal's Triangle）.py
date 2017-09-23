# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/12 14:43'


def generate_PascalTriangle(numRows):
    if numRows == 1:
        return [[1]]
    elif numRows == 2:
        return [[1], [1, 1]]
    elif numRows == 0:
        return []
    else:
        result = [[1], [1, 1]]
        for i in range(3, numRows + 1):
            tmp = [1] * i
            last = result[i - 2]
            for j in range(1, (i - 1) // 2 + 1):
                tmp[j] = tmp[i - 1 - j] = last[j - 1] + last[j]
            result.append(tmp)
        return (result)

print(generate_PascalTriangle(10))