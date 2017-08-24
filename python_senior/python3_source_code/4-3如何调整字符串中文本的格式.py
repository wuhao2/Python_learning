# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 20:39'

import re
# f = open(r'word.txt')
# # lines = f.readlines()
# print(re.sub('(\d{4})-(\d{2})-(\d{2})', r'(\d{4})//(\d{2})//(\d{2})', f))  # 正则表达式的捕获组

inputStr = "hello 123 world 456"
replacedStr = re.sub("\d+", "222", inputStr)
print(replacedStr)
#  结果：hello 222 world 222

