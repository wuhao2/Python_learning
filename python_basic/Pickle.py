# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/9 19:58'

"""使用pickle模块将数据对象保存到文件"""
import pickle

# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}
#
# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)
#
# output = open('data.pkl', 'wb')
#
# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)
#
# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
#
# output.close()

#############################################################
"""使用pickle模块从文件中重构python对象"""

# import pprint, pickle
#
# pkl_file = open('data.pkl', 'rb')
#
# data1 = pickle.load(pkl_file)
# pprint.pprint(data1)
#
# data2 = pickle.load(pkl_file)
# pprint.pprint(data2)
#
# pkl_file.close()


"""预定义的清理行为"""
for line in open("myfile.txt"):
    print(line, end="")
"""以上这段代码的问题是，当执行完毕后，文件会保持打开状态，并没有被关闭。
关键词 with 语句就可以保证诸如文件之类的对象在使用完之后一定会正确的执行他的清理方法"""
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")