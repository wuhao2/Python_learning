# _*_ coding: utf-8 _*_6,
__author__ = 'wuhao'
__date__ = '2017/9/19 19:52'

def numsSun(m, n):
    res = []
    if n <= 0 or m <= 0:
        return
    res.append(n)
    numsSun(m-n, n-1)
    res.pop()
    numsSun(m, n-1)

    return len(res)

if __name__ == "__main__":
    n, m = input("please two integer:").split(' ')
    m = int(m)
    n = int(n)
    if m >= 120 or n >= 120:
            raise Exception("invalid m or n")
    else:
        print(n, m)
    print(numsSun(m, n))