# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 16:39'

s = 'ab;cdd|fdmn\ds|fads;fdsfsd,sdfg|hh\sdfd'
res = s.split(';')
print(res)
# ['ab', 'cdd|fdmn\\ds|fads', 'fdsfsd,sdfg|hh\\sdfd']

res1 =list(map(lambda x: x.split('|'), res))
print(res1)
# [['ab'], ['cdd', 'fdmn\\ds', 'fads'], ['fdsfsd,sdfg', 'hh\\sdfd']]  #列表嵌套列表

t = []  # list.extend(seq) 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
list(map(lambda x: t.extend(x.split('|')), res))
print(t)
# ['ab', 'cdd', 'fdmn\\ds', 'fads', 'fdsfsd,sdfg', 'hh\\sdfd'] #一个列表

###########################################################################################

# 字符串拆分
def mysplit(s, ds):
    res = [s]
    for d in ds:
        extend_list = []
        list(map(lambda x: extend_list.extend(x.split(d)), res))  # python3中需要list（）强转
        res = extend_list
    # return res
    return [x for x in res if x]  # 如果存在连续两个分隔符，结果中会出现‘ ’，所以需要对结果进行过滤
s = 'ab;cdd|fdmn\ds|fads;fdsfsd,,sdfg|hh\sdfd'
print(mysplit(s, ';,\|'))
# result is : ['ab', 'cdd', 'fdmn', 'ds', 'fads', 'fdsfsd', 'sdfg', 'hh', 'sdfd']

#############################################################################################

# 正则表达式拆分
import re
s = 'ab;cdd|fdmn\ds|fads;fdsfsd,,sdfg|hh\sdfd'
print(re.split(r'[,\\;|]+', s))
# 结果：['ab', 'cdd', 'fdmn', 'ds', 'fads', 'fdsfsd', 'sdfg', 'hh', 'sdfd']
