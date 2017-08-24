# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/18 13:15'

from xml.dom.minidom import parse
from xml.dom import minidom
from xml.etree.ElementTree import Element,ElementTree,tostring

e = Element('Data')
e.set('name','abc')
e.text = "123"
print(tostring(e))

e2 = Element("Row")
e3 = Element("Open")
e3.text = '8.80'
e2.append(e3)
print(tostring(e2))
e.append(e2)
e.text = None
print(tostring(e))

et = ElementTree(e)
et.write("../regular_file/test.xml")

# import csv
# def csvToXml(fname):
#     with open(fname,'rb') as fr:
#         reader = csv.reader(fr)
#         headers=reader.next()
#         root=Element('Data')
#         for row in reader:
#             eRow=Element('Row')
#             root.append(eRow)
#             for tag,text in zip(headers,row):
#                 e=Element(str(tag).replace(" ", "_"))
#                 e.text=text
#                 eRow.append(e)
#     pretty(root)
#     return ElementTree(root)
#
#
# def pretty(e, level=0):
#     if len(e) >0:
#         e.text = '\n' + '\t'*(level+1)
#         for child in e:
#             pretty(child,level+1)
#         child.tail = child.tail[:-1]
#     e.tail = '\n' + '\t'*level
#
# et = csvToXml('pingan.csv')
# et.write("pingan.xml")