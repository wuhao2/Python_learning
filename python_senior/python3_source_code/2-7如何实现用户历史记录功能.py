# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 11:12'

# 如何实现用户的历史记录功能
from random import randint
from collections import deque


# N = randint(1, 100)
# print(N)
# history = deque([], 5)
# def guess(k):
#     if k == N:
#         print('right')
#         return True
#     if k < N:
#         print('%s is less-than N' % k)
#     else:
#         print("%s is greater-than N" % k)
#     return False
#
# while True:
#     line = input('please input a number：')
#     if line.isdigit():
#         k = int(line)
#         history.append(k)
#         if guess(k):
#             break
#     elif line == 'h?':
#         print(list(history))



import pickle
q = deque([1, 2, 3, 4, 6], 5)
pickle.dump(q, open('history-record', 'wb'))  # 存储在history-record文件中,序列化

q1 = pickle.load(open('history-record', 'rb'), encoding='latin1')
print(q1)
# 结果： deque([1, 2, 3, 4, 6], maxlen=5)



import pickle
# 序列化
def dump_pickle():
    user = {}
    user['id'] = 1
    user['name'] = 'tanweijie'
    user['email'] = 'tanweijie@outlook.com'
    user['sex'] = 'boy'
    # with保证自动关闭文件
    # 设置文件模式为'wb'来以二进制写模式打开文件
    with open('user.pickle', 'wb') as f:
        # dump()函数接受一个可序列化的Python数据结构
        pickle.dump(user, f)
        print('success')


# 反序列化
def load_pickle():
    with open('user.pickle', 'rb') as f:
        user = pickle.load(f)
        # user变量是一个字典
        print(user)

# 测试序列化与反序列
dump_pickle()
load_pickle()