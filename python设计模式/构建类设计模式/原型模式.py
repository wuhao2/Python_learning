# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/30 21:54'

from copy import copy, deepcopy


class simpleLayer:
    background = [0, 0, 0, 0]
    content = "blank"

    def getContent(self):
        return self.content

    def getBackgroud(self):
        return self.background

    def paint(self, painting):
        self.content = painting

    def setParent(self, p):
        self.background[3] = p

    def fillBackground(self, back):
        self.background = back

    def clone(self):
        return copy(self)

    def deep_clone(self):
        return deepcopy(self)


if __name__ == "__main__":
    dog_layer = simpleLayer()
    dog_layer.paint("Dog")
    dog_layer.fillBackground([0, 0, 255, 0])
    print("Background:", dog_layer.getBackgroud())
    print("Painting:", dog_layer.getContent())
    another_dog_layer = dog_layer.clone()
    print("Background:", another_dog_layer.getBackgroud())
    print("Painting:", another_dog_layer.getContent())

'''
clone和deep_clone有什么区别呢？大多数编程语言中，都会涉及到深拷贝和浅拷贝的问题，
一般来说，浅拷贝会拷贝对象内容及其内容的引用或者子对象的引用，但不会拷贝引用的内容和子对象本身；
而深拷贝不仅拷贝了对象和内容的引用，也会拷贝引用的内容。
所以，一般深拷贝比浅拷贝复制得更加完全，但也更占资源（包括时间和空间资源）
'''