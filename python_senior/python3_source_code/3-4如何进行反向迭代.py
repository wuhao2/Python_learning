# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 15:50'
l = [1, 2, 3, 4]
for x in l:
    print(x, ' ', end='')

# 列表的反向迭代
for x in reversed(l):
    print(x, ' ', end='')

ll = l[::-1]
print(ll)

class FloatRange:
    def __init__(self, start, end, step=0.1):
        self.start = start
        self.end = end
        self.step = step

    def __iter__(self):  # 正向迭代接口
        t = self.start
        while t <= self.end:
            yield t
            t += self.step

    def __reversed__(self):  # 反向迭代接口
        t = self.end
        while t >= self.start:
            yield t
            t -= self.step
# 正向迭代
for x in FloatRange(1.0, 4.0, 0.5):
    print(x, ', ', end='')
# 反向迭代
print()
for x in reversed(FloatRange(1.0, 4.0, 0.5)):
    print(x, ', ', end='')
