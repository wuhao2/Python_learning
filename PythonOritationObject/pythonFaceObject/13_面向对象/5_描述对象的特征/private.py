class A:
    def __init__(self):
        self.__ab = 0

    def info(self):
        print(self.__ab)

a = A()
a.info()
a.__ab = 3
a.info()
print(a.__ab)
