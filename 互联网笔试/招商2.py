# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/13 20:20'
def whoWin():
    m = input("please a integer:")
    m = int(m)
    height = []

    for i in range(m):
        num = input("please input:")
        num = int(num)
        height.append(num)
    print(height)
    A = []
    B = []
    sumA = 0
    sumB = 0
    for i in height:
        if i % 2 == 0:
            A.append(i)
            sumA += i
        else:
            B.append(i)
            sumB += i
    if sumA > sumB:
        print("first one win")
        return True
    else:
        print("second one win")
        return False
print(whoWin())