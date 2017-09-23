def movea():
    print('Move a.')

def moveb():
    print('Move b.')

class MoveObj:
    def set_move(self,moveable):
        self.moveable = moveable

    def move(self):
        self.moveable()


if __name__ == '__main__':
    m = MoveObj()
    m.set_move(movea)
    m.move()
    m.set_move(moveb)
    m.move()
