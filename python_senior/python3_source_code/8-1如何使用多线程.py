# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 20:58'

import requests
from io import StringIO

import csv
from xml.dom import minidom

import time
from threading import Thread

"""
python 中的线程只适合处理IO密集型操作，global interpreter lock导致
Python解释器一次只能执行一个线程，不能实现多cpu并行执行
stringIO是一个支持文件操作的内存对象, IO一般很慢，比如访问网络下载、读写磁盘等
"""
def download(url):
    proxies = {"http": "http://xx.yy.zz.ww:8000"}
    response = requests.get(url, proxies=proxies)
    if response.ok:
        return StringIO(response.content)


"""
将csv文件转换为xml文件是一个cpu密集型操作
"""

def createXmlFromCsv(scsv, fxml):
    root = minidom.Document()
    dataElement = root.createElement("Data")

    reader = csv.reader(scsv)
    headers = reader.next()
    headers = map(lambda h: h.replace(' ', ''), headers)
    for row in reader:
        rowElement = root.createElement("Row")
        for tag, text in zip(headers, row):
            item = root.createElement(tag)
            item.appendChild(root.createTextNode(text))
            rowElement.appendChild(item)
        dataElement.appendChild(rowElement)

    fxml.write(root.appendChild(dataElement).toprettyxml())
    # return root.appendChild(dataElement)


# if __name__ == '__main__':
#     url = "http://table.finance.yahoo.com/table.csv?s=000001.sz"
#     rf = download(url)
#     if rf:
#         with open("000001.xml", 'wb') as wf:
#             createXmlFromCsv(rf, wf)


def handle(sid):
    for sid in range(1, 11):  # 串行下载多支股票数据
        print("Download...%d" % sid)
        url = "http://table.finance.yahoo.com/table.csv?s=%s.sz"
        url %= str(sid).rjust(6, '0')
        rf = download(url)  # 访问网络下载得到csv文件
        if rf is None:
            return
        print('Convert to XML ...(%d)' % sid)
        fname = str(sid).rjust(6, '0') + '.xml'
        with open(fname, 'wb') as wf:
            createXmlFromCsv(rf, wf)  # csv文件转换得到一系列的xml


# 使用thread线程方法1
def handle2(sid):
    print("Counting... %d" % sid)
    for _ in [x for x in range(sid)]:
        time.sleep(0.01)
    print("Counting done %d" % sid)

# t = Thread(target=handle2, args=(1,))  # 创建线程对象
# t.start()  # 执行线程
# t.join() # 等待线程t退出
# print('at last main thread exit ......')


# 使用class类继承Thread, thread线程方法2
class MyThread(Thread):
    def __init__(self, sid):
        super(MyThread, self).__init__()
        self.sid = sid

    def run(self):
        handle2(self.sid)  # 线程处理函数
# 测试1个线程
# t = MyThread(2)
# t.start()

# 测试启动10个线程
threads = []
for i in range(1, 11):
    t = MyThread(i)
    threads.append(t)
    t.start()
for t in threads:
    t.join()  # 等待每一个子线程退出，主线程才退出
print("at last main thread exit.......")



