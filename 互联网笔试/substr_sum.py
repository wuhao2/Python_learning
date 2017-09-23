# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/26 16:00'


def findresult(serial):
    subresults = []
    flag = False
    for i in serial:
        if flag and i < 0:
            flag = False
        elif flag:
            subresults[-1].append(i)
        elif i > 0:
            flag = True
            subresults.append([i])
    return sorted(subresults, key=lambda x: sum(x), reverse=True)[0]


string = {-23, 17, -7, 11, -2, 1, -34}
print(findresult(string))
