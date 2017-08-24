#回形矩阵解题思路:
#1、沿着数字增长顺序,一圈一圈的向内层打印
#2、令每一圈左上端点(p,p),右下(q,q),打印完一层后P++, q++

def snakeMatrix(n):
    m = [[0]*n for i in range(n)] #得到一个二维矩阵
    p = 0
    q = n-1

    temp = 1
    while p < q:
       for i in range(p, q):
           m[p][i] = temp
           temp += 1
       for i in range(p, q):
           m[i][q] = temp
           temp += 1
       for i in range(q, p, -1):
           m[q][i] = temp
           temp += 1
       for i in range(q, p, -1):
           m[i][p] = temp
           temp += 1
       p += 1
       q -= 1

    if p == q:
        m[p][p] = temp
    return m


m = snakeMatrix(8)
for l in m:
    print(l)

