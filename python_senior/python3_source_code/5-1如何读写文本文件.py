# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 22:20'

# s = u'你好'
# print(s.encode('utf8'))  # b'\xe4\xbd\xa0\xe5\xa5\xbd'只有编码成string的字符串才能存储在物理介质中
# print(s.encode('gbk'))  # b'\xc4\xe3\xba\xc3'
# print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf8'))
# print(b'\xc4\xe3\xba\xc3'.decode('gbk'))



# # python2中文本文件的读写  str 和 unicode
# f = open('python2.txt', 'w')
# s = u'你好'
# f.write(s.encode('gbk'))
# f.close()
# f = open('python2.txt', 'r')
# t = f.read()
# print(t.decode('gbk'))



# python3中文本文件读写 bytes 和 str
s = '吴浩'
# 不需要手工编解码
f = open('python3.txt', 'w', encoding='utf8')
f.write('吴浩我爱你')
f.close()
f = open('python3.txt', 'r', encoding='utf8')
s1 = f.read()
print(s1)
