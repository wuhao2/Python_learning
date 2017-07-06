# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/3 18:49'


class Person(object):
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int ')

    def __str__(self):
        return '%s is %s year old'%(self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()

    def __setattr__(self, name, value):
        # setattr(self, name, value)       # RecursionError: maximum recursion depth exceeded
        self.__dict__[name] = value   # success wuhao

    def __getattribute__(self, name):
        # return getattr(self, name)    # RecursionError: maximum recursion depth exceeded
        # return self.__dict__[name]   # RecursionError: maximum recursion depth exceeded
        return super(Person, self).__getattribute__(name)   # success return wuhao


if __name__ == '__main__':
    per1 = Person('wuhao', 24)
    print(per1.name)
    # print(per1)
    # print(dir(per1))

# <__main__.Person object at 0x000001DCE08CD898>
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__',

# define magic method to object convert into string
# wuhao is 24 year old
# ['age', 'name']