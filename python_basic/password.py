# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/9 12:21'

"""
1.遍历字符串

2.取子串，放入set集合

3.最终set集合的长度即是结果
"""
def test():
    passwd = set()
    str = input()
    print(type(str), str)
    lenght = len(str)
    print(len)

    if str == "A":
        # print("1")
        return print(lenght)


    for i in range(0, lenght):
        if i == 0:
            passwd.add(str[i+1:])
        else:
            string = str[:i] + str[i+1:lenght]
            passwd.add(string)

    print(passwd.__str__())
    print(len(passwd))
test()