#分子为1的分数为埃及分数

# 3/7 = 1/3 + 1/11 + 1/231
#a/b - 1/k = a*k - b / b*k


def fun(a,b):
    k = int(b/a)
    if b % a == 0:
        res = "1/%s" %k  #因为要打印成3/7 = 1/3 + 1/11 + 1/231的效果，所有写成字符串
    else:
        k += 1
        res = "1/%s + %s" % (k, fun(a*k - b , b*k)) #递归
    return res

print(fun(4,7))
print(fun(3,7))
print(fun(2,7))
# 1/2 + 1/14
# 1/3 + 1/11 + 1/231
# 1/4 + 1/28