# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 14:49'
def foo(bar=None):
    if bar is None:
        print(bar)

foo()
foo(1)  # True False None都变成关键字

print(b"hello")  # 必须加b才能表示二进制表示
print(u"hello")  # 加u 或者不加u都可以表示正常的字符串

"""python 3中"""
print(0o666)  # 438  ---八进制转十进制
print(oct(438))  # 0o666  ---- 十进制转八进制
print(0b0101)  # 5 ---二进制转十进制
print(bin(438))  # 0b110110110  ---- 十进制转二进制