# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 21:38'

from xml.etree.ElementTree import Element,ElementTree
from xml.dom.minidom import parse
from xml.dom import minidom

from threading import Thread
from io import StringIO
import requests
import csv

# from Queue import  Queue
import queue  # queue线程安全的数据结构，内部已经实现了加锁


from collections import deque  # deque队列是不安全的
# q2 = deque()  # 这个队列是不安全的，在临界区代码出必须加锁，才能保证线程安全
# i = 0


def pretty(e, level=0):
    if len(e) > 0:
        e.text = '\n' + '\t'*(level+1)
        for child in e:
            pretty(child, level+1)
        child.tail = child.tail[:-1]
    e.tail = '\n' + '\t'*level

"""
生产者线程
"""
class DownloadThread(Thread):
    def __init__(self, sid, queue):
        # 经常使用全局变量是不好的设计模式，所以讲queue作为参数传递进来
        Thread.__init__(self)  # 调用父类的构造器
        self.sid = sid
        self.url = "http://table.finance.yahoo.com/table.csv?s=%s.sz"
        self.url %= str(sid).rjust(6, '0')
        self.queue = queue  # queue作为DownloadThread实例属性

    def download(self, url):
        proxies = {"http": "http://135.245.48.34:8000"}
        response = requests.get(url, proxies=proxies)  # 使用代理proxy下载
        # response = requests.get(url)  # 不使用代理下载
        if response.ok:
           return StringIO(response.content)
        f = open("pingan.csv")
        reader = csv.reader(f)
        return StringIO(reader)
        import time
        if self.sid == 1:
            time.sleep(10)
        return StringIO(f.read())

    def run(self):
        print("download ", self.sid, self.url)
        data = self.download(self.url)  # 下载数据
        self.queue.put((self.sid, data))  # 将sid和data入队列，传递给转换线程

"""
消费者线程
"""
class ConvertThread(Thread):
    def __init__(self, queue):  # 传入线程安全队列
        Thread.__init__(self)
        self.queue = queue  # queue作为ConvertThread实例属性

    def createXmlFromCsv(self, scsv, fxml):
        root = minidom.Document()
        dataElement = root.createElement("Data")

        reader = csv.reader(scsv)
        headers = reader.next()
        headers = map(lambda h: h.replace(' ',''), headers)
        for row in reader:
            rowElement = root.createElement("Row")
            for tag, text in zip(headers,row):
                item=root.createElement(tag)
                item.appendChild(root.createTextNode(text))
                rowElement.appendChild(item)
            dataElement.appendChild(rowElement)
        fxml.write(root.appendChild(dataElement).toprettyxml())
        # return root.appendChild(dataElement)

    def csvToXml(self, scsv, fname):
        reader = csv.reader(scsv)
        headers = reader.next()
        root = Element('Data')
        for row in reader:
            eRow = Element('Row')
            root.append(eRow)
            for tag, text in zip(headers,row):
                e = Element(str(tag).replace(" ", "_"))
                e.text = text
                eRow.append(e)
        pretty(root)
        et = ElementTree(root)
        et.write(fname)

    def run(self):
        print("xxyy....in csv thread")
        while True:
            import time
            print("xxyyzz....in csv thread", time.localtime())
            sid, data = self.queue.get()
            # 从队列中取数据，取得一个元组，然后对tuple拆包
            print("after getting xxyyzz....in csv thread", time.localtime)
            if sid == -1:
                break  # sid=-1时，退出while循环
            if data:
                print('Convert to XML ...(%d)' % sid)
                fname = str(sid).rjust(6, '0') + '.xml'  # 转换得到的xml文件名
                with open(fname, 'wb') as wf:
                    self.createXmlFromCsv(data, wf)
                    # self.csvToXml(data,wf)

# 测试
if __name__ == '__main__':
    q = queue.Queue()
    dThreads = [DownloadThread(i, q) for i in range(1, 4)]  # 创建4个下载线程
    cThreads = ConvertThread(q)  # 创建1个转换线程

    for t in dThreads:
        t.start()  # 开启4个下载线程

    cThreads.start()  # 开启转换线程

    for t in dThreads:
        t.join()   # 等待所有的下载线程执行完

    print("............main thread...............")
    q.put((-1, None))