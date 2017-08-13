# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/9 21:05'


"""os模块提供了不少与操作系统相关联的函数。"""
import os
os.getcwd()
os.chdir("")
os.chdir("")
os.system('mkdir today')
dir(os)
help(os)

"""针对日常的文件和目录管理任务"""
import shutil

shutil.copyfile('data.db', 'archive.db')
shutil.move('/build/executables', 'installdir')


"""
文件通配符
glob模块提供了一个函数用于从目录通配符搜索中生成文件列表"""
import glob
glob.glob('*.py')
# ['primes.py', 'random.py', 'quote.py']


"""命令行参数
通用工具脚本经常调用命令行参数。这些命令行参数以链表形式存储于 sys 模块的 argv 变量。
例如在命令行中执行 "python demo.py one two three" 后可以得到以下输出结果:
"""
import sys
print(sys.argv)
# ['demo.py', 'one', 'two', 'three']

"""
字符串正则匹配
re模块为高级字符串处理提供了正则表达式工具。对于复杂的匹配和处理，正则表达式提供了简洁、优化的解决方案:
"""
import re
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
# ['foot', 'fell', 'fastest']
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
# 'cat in the hat
"""
如果只需要简单的功能，应该首先考虑字符串方法，因为它们非常简单，易于阅读和调试:
"""
'tea for too'.replace('too', 'two')
# 'tea for two'


"""
random提供了生成随机数的工具。
"""
import random
random.choice(['apple', 'pear', 'banana']) # 随机选择
random.sample(range(100), 10)  # 随机采样
random.random()    # random float
random.randrange(6)    # random integer chosen from range(6)
import random
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())
# 生成同一个随机数
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())
# 生成同一个随机数
random.seed( 10 )
print ("Random number with seed 10 : ", random.random())



"""
访问 互联网
有几个模块用于访问互联网以及处理网络通信协议。
其中最简单的两个是用于处理从 urls 接收的数据的 urllib.request
以及用于发送电子邮件的 smtplib:
"""
from urllib.request import urlopen
for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
    line = line.decode('utf-8')  # Decoding the binary data to text.
    if 'EST' in line or 'DET' in line:  # look for Eastern Time
        print(line)
# <BR>Nov. 25, 09:43:32 PM EST

import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('soothsayer@example.org', 'jcaesar@example.org')
"""
To: jcaesar@example.org
From: soothsayer@example.org
Beware the Ides of March.
"""
# 注意第二个例子需要本地有一个在运行的邮件服务器。


"""
日期和时间
datetime模块为日期和时间处理同时提供了简单和复杂的方法。
支持日期和时间算法的同时，实现的重点放在更有效的处理和格式化输出。
该模块还支持时区处理:
"""
from datetime import date, datetime
now = date.today()
print(now)
datetime.date(2003, 12, 1)
now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B.")

birthday = date(1991, 10, 12)
age = now - birthday
age.days

"""
数据压缩
以下模块直接支持通用的数据打包和压缩格式：
zlib，gzip，bz2，zipfile，以及 tarfile。
"""
import zlib
s = b'witch which has which witches wrist watch'
print(len(s))
t = zlib.compress(s)
print(len(t))
zlib.decompress(t)
print(zlib.crc32(s))


"""
性能度量
有些用户对了解解决同一问题的不同方法之间的性能差异很感兴趣。
Python 提供了一个度量工具，为这些问题提供了直接答案。
例如，使用元组封装和拆封来交换元素看起来要比使用传统的方法要诱人的多,
timeit 证明了现代的方法更快一些
"""
from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())



"""测试模块"""
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # 自动验证嵌入测试


import unittest

class TestStatisticalFunctions(unittest.TestCase):

    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        self.assertRaises(ZeroDivisionError, average, [])
        self.assertRaises(TypeError, average, 20, 30, 70)

unittest.main() # Calling from the command line invokes all tests