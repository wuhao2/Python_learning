# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/20 10:42'


from xml.etree.ElementTree import Element,ElementTree
from xml.dom.minidom import parse
from xml.dom import minidom

from threading import Thread, Event
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
    def __init__(self, queue, cEvent, tEvent):  # 传入线程安全队列
        Thread.__init__(self)
        self.queue = queue  # queue作为ConvertThread实例属性
        self.cEvent = cEvent
        self.tEvent = tEvent

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
        count = 0
        print("xxyy....in csv thread")
        while True:
            import time
            print("xxyyzz....in csv thread", time.localtime())
            sid, data = self.queue.get()
            # 从队列中取数据，取得一个元组，然后对tuple拆包
            print("after getting xxyyzz....in csv thread", time.localtime)

            if sid == -1:
                self.cEvent.set()  # 转换退出时，就算只有两个文件也要，打包
                self.cEvent.wait()  # 等待打包完成
                break  # sid=-1时，退出while循环
            if data:
                print('Convert to XML ...(%d)' % sid)
                fname = str(sid).rjust(6, '0') + '.xml'  # 转换得到的xml文件名
                with open(fname, 'wb') as wf:
                    self.createXmlFromCsv(data, wf)
                    # self.csvToXml(data,wf)

                count += 1
                if count == 5:
                    self.cEvent.set()  # 已经存在5个xml文件了。通知 开始打包
                    # 此时不能干扰打包程序执行，需要等待阻塞
                    self.tEvent.wait()
                    self.tEvent.clear()
                    count = 0

"""
打包线程
"""


class TarThread(Thread):
    def __init__(self, cEvent, tEvent):
        Thread.__init__(self)
        self.count = 0
        self.cEvent = cEvent
        self.tEvent = tEvent
        self.setDaemon(True)  # 将打包线程设置成守护线程

    def tarXml(self):
        self.count += 1
        tfname = '%d.tgz' % self.count
        tf = tarfile.open(tfname, "w:gz")
        for fname in os.listdir('.'):
            if fname.endswith('.xml'):
                tf.add(fname)
                os.remove(fname)
        tf.close()
        if not tf.members:
            os.remove(tfname)

    def run(self):
        while True:
            self.cEvent.wait()  # 等待 csv文件转换成xml文件 完毕
            self.tarXml()  # 打包
            self.cEvent.clear()  # 为了重复使用event事件

            self.tEvent.set()  # 通知 继续 csv文件转换成xml文件


# 测试
if __name__ == '__main__':
    q = queue.Queue()  # 创建 线程通信 安全队列
    cEvent = Event()
    tEvent = Event()  # 创建事件 cEvent， tEvent

    dThreads = [DownloadThread(i, q) for i in range(1, 4)]  # 创建4个下载线程
    cThread = ConvertThread(q, cEvent, tEvent)  # 创建1个转换线程
    tThread = TarThread(cEvent, tEvent)   # 创建一个打包线程

    tThread.start()  # 开启打包线程
    for t in dThreads:
        t.start()  # 开启4个下载线程
    cThread.start()  # 开启转换线程

    for t in dThreads:
        t.join()   # 等待所有的下载线程执行完

    print("............main thread...............")
    q.put((-1, None))  #











# import tarfile
# import os
# from threading import Thread
# def tarXml(tfname):
#     tf = tarfile.open(tfname, "w:gz")
#     # for fname in os.listdir('../regular_file'):  # 遍历regular_file目录中的所有文件
#     for fname in os.listdir('.'):  # 遍历当前目录中的所有文件
#         if fname.endswith('.xml'):  # 找到xml文件
#             tf.add(fname)  # 加入到tar文件中
#             # os.remove(fname)  # 删除
#     tf.close()
#     if not tf.members:  # 如果目录中一个xml文件都没有，则tar包也是空的，删除掉tar包
#         os.remove(tfname)
#     print("done tar......")
# tarXml('test.tgz')




