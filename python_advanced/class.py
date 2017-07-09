# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/7/3 17:54'


class Person(object):
    hobby = 'play computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @staticmethod
    def learn():
        print("i love python")

    @classmethod
    def get_hobby(cls):
        return cls.hobby

    @property
    def get_weight(self):
        return self.__weight

    @property
    def get_age(self):
        return self._age

    def self_introduction(self):
        print("hello i am haowu2")


class ForeignPerson(Person):
    def __init__(self, name, age, weight, language):
        super(ForeignPerson, self).__init__(name=name, age=age, weight=weight)
        self.language = language

    def self_introduction(self):
        print("hi. i am a foreigner")

def introduction(person):
    if isinstance(person, Person):
        person.self_introduction()


if __name__ == '__main__':
    Person.learn()  # no need instance, call static method
    person = ForeignPerson("wuhao", 25, '130', 'English') # instance
    print(person.__doc__)
    print(person.__dir__())
    print(person.__dict__)
    print(person.name, "\t", person.hobby, person.language)
    print(person.get_hobby())
    print(person.get_weight)
    person.self_introduction()

    # execute the same method , reflect many status
    person1 = Person("wuhao", 21, '130')
    foreigner = ForeignPerson("sunny", 25, '65', 'english')
    introduction(person1)
    introduction(foreigner)
