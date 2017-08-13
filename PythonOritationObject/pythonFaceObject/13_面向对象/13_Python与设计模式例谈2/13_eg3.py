def deco(a_class):
    class NewClass:
        def __init__(self,age,color):
            self.wrapped = a_class(age)
            self.color = color
        def display(self):
            print(self.color)
            print(self.wrapped.age)
    return NewClass

@deco
class Cat:
    def __init__(self,age):
        self.age = age

    def display(self):
        print(self.age)

if __name__ == '__main__':
    c = Cat(12,'black')
    c. display()