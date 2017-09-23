# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/10 20:57'

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
    # print('{0} {1} {2}'.format(x, x*x, x*x*x))

a = int(input("input:"))
print(a, type(a))

"""

1、在python2.x中raw_input( )和input( )，两个函数都存在，其中区别
raw_input( )---将所有输入作为字符串看待，返回字符串类型
input( )-----只能接收“数字”的输入，在对待纯数字输入时具有自己的特性，
它返回所输入的数字的类型（ int, float ）

2、在python3.x中raw_input( )和input( )进行了整合，去除了raw_input( )，
仅保留了input( )函数，其接收任意任性输入，将所有输入默认为字符串处理，并返回字符串类型。

"""

print('{0},{1}'.format('zhangk', 32))
print('{},{},{}'.format('zhangk', 'boy', 32))
print('{name},{sex},{age}'.format(age=32, sex='male', name='zhangk'))
# zhangk,32
# zhangk,boy,32
# zhangk,male,32
# 格式限定符
# 它有着丰富的的“格式限定符”（语法是{}中带:号），比如：
# 填充与对齐
# 填充常跟对齐一起使用
# ^、<、>分别是居中、左对齐、右对齐，后面带宽度
# :号后面带填充的字符，只能是一个字符，不指定的话默认是用空格填充
print('{:>8}'.format('zhang'))
print('{:0>8}'.format('zhang'))
print('{:a<8}'.format('zhang'))
print('{:p^10}'.format('zhang'))

# 精度与类型f
# 精度常跟类型f一起使用
print('{:.2f}'.format(31.31412))

# 其他类型
# 主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制
print('{:b}'.format(15))
print('{:d}'.format(15))
print('{:o}'.format(15))
print('{:x}'.format(15))
# 用逗号还能用来做金额的千位分隔符

print('{:,}'.format(123456789))
