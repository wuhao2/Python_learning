# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/3 18:49'


class Person(object):
    def __new__(cls, *args, **kwargs):
        print('call __new__ method')
        print(args)
        return super(Person, cls).__new__(cls)

    def __init__(self, name, age):
        print('call __init__ method')
        self.name = name
        self.age = age

if __name__ == '__main__':
    per = Person('wuhao', 24)
    print(per.__dict__)

# instance process
# call __new__ method
# ('wuhao', 24)
# call __init__ method
# {'age': 24, 'name': 'wuhao'}