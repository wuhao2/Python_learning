# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 13:40'

# l = [1, 2, 3, 4]
# print(l.__iter__())  # 返回迭代器对象
# for i in l:
#     print(i)

# import requests
# def getWeather(city):
#     r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
#     data = r.json()['data']['forecast'][0]
#     return '%s: %s, %s' % (city, data['low'], data['high'])
# print(getWeather(u'北京'))
# print(getWeather(u'上海'))
# 北京: 低温 22℃, 高温 31℃
# 上海: 低温 26℃, 高温 33℃


import requests
from collections import Iterable, Iterator  # 实现一个可迭代对象与迭代器对象

# 气温迭代器类
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    # def next(self):
    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return self.getWeather(city)

    def getWeather(self, city):
        r = requests.get(u'http://wthrcdn.etouch.cn/weather_mini?city=' + city)
        data = r.json()['data']['forecast'][0]
        return '%s: %s, %s' % (city, data['low'], data['high'])

# 可迭代对象类
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)

# 测试,实现用时访问
for x in WeatherIterable([u'北京', u'上海', u'广州', u'武汉', u'深圳', u'杭州']):
    print(x)


# 北京: 低温 22℃, 高温 31℃
# 上海: 低温 26℃, 高温 33℃
# 广州: 低温 28℃, 高温 35℃
# 武汉: 低温 25℃, 高温 32℃
# 深圳: 低温 28℃, 高温 33℃
# 杭州: 低温 26℃, 高温 35℃
