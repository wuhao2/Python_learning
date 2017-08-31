# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/22 9:31'

# a = 2
# b = 3
# a = a + b
# b = a -b
# a = a - b

# a = a * b
# b = a/b
# a = a/b

# a = a^b
# b = a^b
# a = a^b

# print('a:',a, 'b:', b)

'''
python3.5
1、Python中的ord及chr函数指的就是通常意义的unicode，即2个字节
2、UTF-8是1-6个字节的可变长编码方式，
常用的英文字母被编码成1个字节，汉字通常是3个字节，只有很生僻的字符才会被编码成4-6个字节
'''
# NumOctHex.py
# 自己写一个模块NumOctHex.py，包含8、10、16转换成2进制
'''
str_num的类型必需是可被str转换的整数，如：‘111’、‘123’
16进制中str_num可以是‘123456789abcdef’，且必须是0-9及a-f之间
8进制中str_num可以是‘1234567’，且必须是0-7之间的数
'''
'''
系统自带的转换方法都是通过10进制进行转换的，下面的三个函数是通过将8、10、16转换成2进制
'''


# 十进制to二进制
def dec2bin(str_num):
    num = int(str_num, 8)
    bit = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        bit.append(str(rem))
    return ''.join(bit[::-1])


# 八进制to二进制
def oct2bin(str_num):
    num = int(str_num, 8)
    bit = []
    while True:
        if num == 0: break
        num, rem = divmod(num, 2)
        bit.append(str(rem))
    return ''.join(bit[::-1])


print(dec2bin(str(ord('中'))))
