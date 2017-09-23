# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/9/16 16:38'
import platform
print('Python', platform.python_version())

try:
    let_us_cause_a_NameError
# except NameError,err:  # python 2.7异常
except NameError as err:  # python3 异常必须使用as关键字
    print(err, '--> our error message')
