# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 16:16'
import io

# f = io.open("foofoo.txt", "rb")
# print(f)  # 返回一个文件句柄 <_io.BufferedReader name='foofoo.txt'>
# f.close()
#
# f = open('foofoo.txt', 'rb')
# line = f.readline() # 默认只读取第一行
# print(line)
# f.close()

# f = open('foofoo.txt','rb')
# for line in open('foofoo.txt'):
#    line = f.readline()  # 逐行读取
#    print (line)
# f.close()

f = open('foofoo.txt', 'rb')
for line in f.readlines():
  print (line)
f.close()
# result：
# b'hello world\r\n'
# b'hello world\r\n'
# b'hello world\r\n'
# b'hello world\r\n'

f = open('foofoo.txt', 'rb')
print(f.read())  # b'hello world\r\nhello world\r\nhello world\r\nhello world\r\n'
f.close()
