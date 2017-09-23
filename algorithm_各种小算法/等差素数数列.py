# 等差素数数列

def findAllPrime(n):
    pt = [True] * n
    prime = []

    for p in range(2, n):
        if not pt[p]:
            continue
        prime.append(p)

        for i in range(p * p, n, p):
            pt[i] = False
    return prime, pt


def equalDifferenceSeries(pt, prime):
    for i in range(len(prime)):
        for j in range(i + 1, len(prime)):
            a0, a1 = prime[i], prime[j]
            an = a1 + a1 - a0  # 等差数列的公式，计算得到an
            s = []  # 用来存放an
            while an < 100 and pt[an]:  # 后面一个条件是依赖第一个条件的
                s.append(an)
                an = an + (a1 - a0)  # 计算下一个an，也就是an+1 = an + 公差
            if s:
                print([a0, a1] + s)  # 列表相加


prime, pt = findAllPrime(100)
print(prime)
equalDifferenceSeries(pt, prime)
