class A:
    def __init__(self):
        self._ab = 0

    def info(self):
        print(self._ab)

a = A()
a.info()
a._ab = 3
a.info()
print(a._ab)
