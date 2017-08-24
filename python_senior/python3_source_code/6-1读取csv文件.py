# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 10:46'

"""
将pingan1.csv中的文件写进pingan2.csv中
"""
import os
# import urllib.request
# def cbk(a, b, c):
#     '''
#     回调函数
#     @a:已经下载的数据块
#     @b:数据块的大小
#     @c:远程文件的大小
#     '''
#     per = 100.0*a*b/c
#     if per > 100:
#         per = 100
#     print('%.2f%%' % per)
#
# url = 'http://table.finance.yahoo.com/table.csv?s=000001.sz'
# dir = os.path.abspath('.')
# work_path = os.path.join(dir, 'python_senior')
# urllib.request.urlretrieve(url, work_path, cbk)


import csv

with open('pingan1.csv', 'rb') as rf:
    reader = csv.reader(rf)  # 返回一个迭代器，返回的值放入list中
    with open('pingan2.csv', 'wb') as wf:
        writer = csv.writer(wf)
        headers = reader.next()
        writer.writerow(headers)

        for row in reader:
            if row[0] < '2016-01-01':
                break
            if int(row[5]) >= 50000000:
                writer.writerow(row)
print('done')


"""
it is ok, success running
"""
# 方式1：没有指定存放路径与下载时的状态，
# import urllib.request
# data = urllib.request.urlretrieve("http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2")

# 方式2：
# import os
# import urllib.request
#
# def cbk(a,b,c):
#     '''''回调函数
#     @a:已经下载的数据块
#     @b:数据块的大小
#     @c:远程文件的大小
#     '''
#     per=100.0*a*b/c
#     if per>100:
#         per=100
#     print ('%.2f%%' % per)
#
# url='http://www.python.org/ftp/python/2.7.5/Python-2.7.5.tar.bz2'
# dir=os.path.abspath('.')
# work_path=os.path.join(dir, 'Python-2.7.5.tar.bz2')
# urllib.request.urlretrieve(url, work_path, cbk)