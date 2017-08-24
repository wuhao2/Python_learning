# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 21:24'
d = {
    "lodsdf": 100.0,
    "lodvbsdf": 10.3,
    "lodfdfdfsdf": 13.3,
    "df": 1002.2,
    "wef": 110.7
}
print(d)
w = max(map(len, d.keys()))  # 找到字符串中长度最大的一个
for k in d:
    print(k.ljust(w), ":", d[k])
    # ljust(s, "=")用=填充
    # format(s, '<20') 左对齐
    # format(s, '>20') 右对齐
    # format(s, '^20') 居中

#结果：
# lodvbsdf    : 10.3
# lodfdfdfsdf : 13.3
# wef         : 110.7
# lodsdf      : 100.0
# df          : 1002.2