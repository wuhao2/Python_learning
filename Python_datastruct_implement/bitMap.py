# _*_ coding: utf-8 _*_
__author__ = 'bobby'
__data__ = '2017/6/4 15:40 '


# bitmap的排序、
class Bitmap():
    def __init__(self, max):  # 首先要计算需要多少个数组，所以传入一个最大的数
        self.size = int((max + 31 - 1) / 31)  # 计算需要多少个数组的公式
        self.array = [0 for i in range(self.size)]  # 初始化bitmap，零

    def bitIndex(self, num):  # 位索引
        return num % 31  # 求余

    def set(self, num):
        elemIndex = int(num / 31)  # 确定在第几个数组中，必须强制转换成int
        byteIndex = self.bitIndex(num)  # 具体在数组中的第几位
        elem = self.array[elemIndex]  # 选择哪个数组进行操作
        self.array[elemIndex] = elem | (1 << byteIndex)  # 置1

    # 根据bitmap从左到右排序
    def test(self, i):
        elemIndex = int(i / 31)  # 必须强制转换成int
        byteIndex = self.bitIndex(i)
        if self.array[elemIndex] & (1 << byteIndex):
            return True
        return False


if __name__ == '__main__':
    MAX = ord('z')  # 将z转化为ASSIC码
    suffle_array = [x for x in 'coledraw']  # 将字符串进行拆分出来
    result = []
    bitmap = Bitmap(MAX)
    for c in suffle_array:  # 遍历数组
        bitmap.set(ord(c))
    for i in range(MAX + 1):
        if bitmap.test(i):
            result.append(chr(i))

    print("原始数组为：%s" % suffle_array)
    print("排序后的数组为：%s" % result)
