#回文数就是1234578 ---->8754321

def isPolindromeNum(n):
    a = []
    while n>0:
        a.append(n%10) #取最后一位
        n = int(n/10)
    print(a)

    for i in range(int(len(a)/2)):
        if a[i] != a[-i -1]:  #就是a[0] = a[-1]; a[1] = a[-2] .....
            return False
    return True

print(isPolindromeNum(1234321))
print(isPolindromeNum(324551))
# [1, 2, 3, 4, 3, 2, 1]
# True
# [1, 5, 5, 4, 2, 3]
# False