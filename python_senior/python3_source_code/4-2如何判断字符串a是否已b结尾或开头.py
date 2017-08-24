# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/17 20:22'

# s = '2-5如何快速查找多个字典中的公共键.py'
# s.startswith(('2'))
# s.endswith(('.py'))

import os, stat
l = [fileName for fileName in os.listdir('.') if fileName.endswith(('.sh', '.py'))]  # 列出所有的文件.py .sh
print(l)

print(os.stat('2-3如何统计序列中每个元素出现的频率.py').st_mode)    # 查看权限33206
print(oct(os.stat('2-3如何统计序列中每个元素出现的频率.py').st_mode))  # 转换为8进制0o100666
print(os.chmod('2-3如何统计序列中每个元素出现的频率.py', os.stat('2-3如何统计序列中每个元素出现的频率.py').st_mode | stat.S_IXUSR))  # 增加可执行权限

