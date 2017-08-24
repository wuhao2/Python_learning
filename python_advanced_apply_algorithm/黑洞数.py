# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/9 11:06 '
"""
1.问题描述:
黑洞数又称陷阱数，是类具有奇特转换特性的整数。任何一个数字不全相同的整数，经有限“重排求差”操作，总会得到某一
个或一些数，这些数即为黑洞数。“重排求差”操作即把组成该数的数字重排后得到的最大数减去重排后得到的最小数。
举个例子，3位数的黑洞数为495.
简易推导过程：随便找个数，如297,3个位上的数从小到大和从大到小各排一次，为972和279，相减得693。按上面做法再做一次，得到594，再做一次，得到495，之后反复都得到495。

验证4位数的黑洞数为6174。
"""

#黑洞数：297这个三位数，重排最大为972，重排最小为279，二者相减972 - 279 = 693，循环查找
#list = [2, 7, 9]利用列表排序， list[::-1]列表切片变成[9, 7, 2]
#

def fun(n):
    print(n)#用于打印每次递归开始时，这个数的值
    a = []
    temp = n
    while temp>0:
        a.append(temp%10)
        temp = int(temp/10)
    a.sort()#重排,从小到大

    #972
    s1 = 0
    for x in a[::-1]:
        s1 = s1*10 + x
    #297
    s2 = 0
    for x in a:
        s2 = s2*10 + x

    if s1 - s2 == n:#求差=n, 则递归结束
        return n
    else:
        return fun(s1-s2)#递归循环，继续查找黑洞数

#test，输入一个数297，寻找它的黑洞数
# res = fun(297)
# print('res:', res)
# 最后得到黑洞数495，，，，954-459=495
# 297
# 693
# 594
# 495
# res: 495


from functools import reduce
def fun1(n):
    a = [int(c) for c in str(n)]
    a.sort()
    s1 = reduce(lambda x, y: 10 * x + y, a[::-1])
    s2 = reduce(lambda x, y: 10 * x + y, a)
    return n if s1 - s2 == n else fun(s1 - s2)
res = fun1(295)
print ('res : ', res)


"""
三个函数比较类似，都是应用于序列的内置函数。常见的序列包括list、tuple、str。
1.map函数
map函数会根据提供的函数对指定序列做映射。
map函数的定义：
map(function, sequence[, sequence, ...]) -> list
通过定义可以看到，这个函数的第一个参数是一个函数，剩下的参数是一个或多个序列，返回值是一个集合。
function可以理解为是一个一对一或多对一函数，map的作用是以参数序列中的每一个元素调用function函数，返回包含每次function函数返回值的list。
比如要对一个序列中的每个元素进行平方运算：
map(lambda x: x ** 2, [1, 2, 3, 4, 5])
返回结果为：
[1, 4, 9, 16, 25]
在参数存在多个序列时，会依次以每个序列中相同位置的元素做参数调用function函数。
比如要对两个序列中的元素依次求和。
map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
map返回的list中第一个元素为，参数序列1的第一个元素加参数序列2中的第一个元素(1 + 2)，
list中的第二个元素为，参数序列1中的第二个元素加参数序列2中的第二个元素(3 + 4)，
依次类推，最后的返回结果为：
[3, 7, 11, 15, 19]
要注意function函数的参数数量，要和map中提供的集合数量相匹配。
如果集合长度不相等，会以最小长度对所有集合进行截取。
当函数为None时，操作和zip相似：
map(None, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
返回结果为：
[(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]

2.filter函数
filter函数会对指定序列执行过滤操作。
filter函数的定义：
filter(function or None, sequence) -> list, tuple, or string
function是一个谓词函数，接受一个参数，返回布尔值True或False。
filter函数会对序列参数sequence中的每个元素调用function函数，最后返回的结果包含调用结果为True的元素。
返回值的类型和参数sequence的类型相同
比如返回序列中的所有偶数：
def is_even(x):
return x & 1 != 0

filter(is_even, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
返回结果为：
[1, 3, 5, 7, 9]
如果function参数为None，返回结果和sequence参数相同。

3.reduce函数
reduce函数，reduce函数会对参数序列中元素进行累积。
reduce函数的定义：
reduce(function, sequence[, initial]) -> value
function参数是一个有两个参数的函数，reduce依次从sequence中取一个元素，和上一次调用function的结果做参数再次调用function。
第一次调用function时，如果提供initial参数，会以sequence中的第一个元素和initial作为参数调用function，否则会以序列sequence中的前两个元素做参数调用function。
reduce(lambda x, y: x + y, [2, 3, 4, 5, 6], 1)
结果为21(  (((((1+2)+3)+4)+5)+6)  )
reduce(lambda x, y: x + y, [2, 3, 4, 5, 6])
结果为20

"""