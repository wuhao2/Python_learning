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

    def __eq__(self, other):
        if isinstance(other, Person):
            if self.age == other.age:
                return True
            else:
                return False
        else:
            raise Exception('the type of object must be Person')

    def __add__(self, other):
        if isinstance(other, Person):
            return self.age + other.age
        else:
            raise Exception('the type of object must be Person')


if __name__ == '__main__':
    per1 = Person('wuhao', 24)
    per2 = Person('sunny', 25)
    print(per1 == per2)
    print(per1 + per2)


# False
# 49

