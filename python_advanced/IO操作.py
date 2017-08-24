# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/21 10:39'
"""
第一种是CPU等着，也就是程序暂停执行后续代码，等100M的数据在10秒后写入磁盘，
再接着往下执行，这种模式称为同步IO；

另一种方法是CPU不等待，只是告诉磁盘，“您老慢慢写，不着急，我接着干别的事去了”，
于是，后续代码可以立刻接着执行，这种模式称为异步IO。

同步和异步的区别就在于是否等待IO执行的结果。好比你去麦当劳点餐，
你说“来个汉堡”，服务员告诉你，对不起，汉堡要现做，需要等5分钟，
于是你站在收银台前面等了5分钟，拿到汉堡再去逛商场，这是同步IO。

你说“来个汉堡”，服务员告诉你，汉堡需要等5分钟，你可以先去逛商场，
等做好了，我们再通知你，这样你可以立刻去干别的事情（逛商场），这是异步IO。

很明显，使用异步IO来编写程序性能会远远高于同步IO，但是异步IO的缺点是编程模型复杂。
想想看，你得知道什么时候通知你“汉堡做好了”，而通知你的方法也各不相同。
如果是服务员跑过来找到你，这是回调模式，如果服务员发短信通知你，
你就得不停地检查手机，这是轮询模式。总之，异步IO的复杂度远远高于同步IO。
"""
# with open('/path/to/file', 'r') as f:
#     print(f.read())
    # 调用read()会一次性读取文件的全部内容，如果文件有10G，
    # 内存就爆了，所以，要保险起见，可以反复调用read(size)方法，
    # 每次最多读取size个字节的内容。另外，调用readline()可以每次读取一行内容，
    # 调用readlines()一次读取所有内容并按行返回list。因此，要根据需要决定怎么调用。
    # 如果文件很小，read()一次性读取最方便；如果不能确定文件大小，
    # 反复调用read(size)比较保险；如果是配置文件，调用readlines()最方便：
    # f = open('/Users/michael/test.jpg', 'rb')

    # 字符编码
    # 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，
    # 例如，读取GBK编码的文件：
    # f = open('/Users/michael/gbk.txt', 'r', encoding='gbk')

    # 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，
    # 因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，
    # open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。
    # 最简单的方式是直接忽略：
    # f = open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')


"""
StringIO

很多时候，数据读写不一定是文件，也可以在内存中读写。
StringIO顾名思义就是在内存中读写str。
要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即
"""
from io import StringIO
f = StringIO()
f.write('hello')
f.write('wuhao')
print(f.getvalue())  # hellowuhao,获得写入后的str

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取：
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
    s = f.readline()
    if s == '':
       break
    print(s.strip())

"""
BytesIO

StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。
BytesIO实现了在内存中读写bytes，我们创建一个BytesIO，然后写入一些bytes：
"""
from io import BytesIO
f = BytesIO()
f.write('中国'.encode('utf-8'))
print(f.getvalue())  # b'\xe4\xb8\xad\xe5\x9b\xbd'

# 请注意，写入的不是str，而是经过UTF-8编码的bytes。
# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())  # b'\xe4\xb8\xad\xe6\x96\x87'

############################################################
import os
os.name
# os.uname()
os.environ
os.environ.get('PATH')

# 查看当前目录的绝对路径:
abspath = os.path.abspath('.')
print(abspath)

# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
testdir = os.path.join('.', 'testdir')
print(testdir)
os.mkdir('testdir')  # 然后创建一个目录:
os.rmdir('testdir')  # 删掉一个目录:

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，
# os.path.join()返回这样的字符串：part-1/part-2
# 而Windows下会返回这样的字符串：part-1\part-2

#拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，
# 这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名

# 对文件重命名:
# os.rename('test.txt', 'test.py')
# 删掉文件:
# os.remove('test.py')
#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
l = [x for x in os.listdir('.') if os.path.isdir(x)]
l1 = [x for x in os.listdir('.') if os.path.isfile(x)
                                and os.path.splitext(x)[1]=='.py']
print(l, '\n', l1)



###########################################################################
# 幸运的是shutil模块提供了copyfile()的函数，
# 你还可以在shutil模块中找到很多实用函数，
# 它们可以看做是os模块的补充。
import shutil
shutil.copyfileobj(open('old.xml','r'), open('new.xml', 'w'))  # 将文件内容拷贝到另一个文件中
shutil.copyfile('f1.log', 'f2.log')  # 拷贝文件
shutil.copymode('f1.log', 'f2.log')  # 仅拷贝权限。内容、组、用户均不变
shutil.copystat('f1.log', 'f2.log')  # 仅拷贝状态的信息，包括：mode bits, atime, mtime, flags
shutil.copy('f1.log', 'f2.log')  # 拷贝文件和权限
shutil.copy2('class.py', 'temp.py')  # 拷贝文件和状态信息
# 递归的去拷贝文件夹
shutil.copytree('folder1', 'folder2', ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
shutil.copytree('f1', 'f2', symlinks=True, ignore=shutil.ignore_patterns('*.pyc', 'tmp*'))
# 递归的去删除文件
shutil.rmtree('folder1')
# 递归的去移动文件，它类似mv命令，其实就是重命名。
shutil.move('folder1', 'folder3')

#将 当前目录 下的文件打包放置 当前目录
ret = shutil.make_archive("./package", 'gztar', root_dir='.')


import zipfile
# 压缩
z = zipfile.ZipFile('laxi.zip', 'w')
z.write('a.log')
z.write('data.data')
z.close()
# 解压
z = zipfile.ZipFile('laxi.zip', 'r')
z.extractall()
z.close()
import tarfile
# 压缩
tar = tarfile.open('your.tar', 'w')
tar.add('/Users/wupeiqi/PycharmProjects/bbs2.log', arcname='bbs2.log')
tar.add('/Users/wupeiqi/PycharmProjects/cmdb.log', arcname='cmdb.log')
tar.close()
# 解压
tar = tarfile.open('your.tar', 'r')
tar.extractall()  # 可设置解压地址
tar.close()

################################################################################

