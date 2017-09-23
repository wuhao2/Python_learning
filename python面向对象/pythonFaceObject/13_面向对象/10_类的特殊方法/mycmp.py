class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __lt__(self,oth):
        return self.x < oth.x

    def __gt__(self,oth):
        return self.y > oth.y

if __name__ == '__main__':
    pa = Point(0,1)
    pb = Point(1,0)
    print(pa < pb)
    print(pa > pb)