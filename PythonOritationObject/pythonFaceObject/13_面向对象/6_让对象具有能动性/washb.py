class Washer:

    def __init__(self,water=10,scour=2):
        self.water = water
        self.scour = scour

    def set_water(self,water):
        self.water = water

    def set_scour(self,scour):
        self.scour = scour

    def add_water(self):
        print('Add water:',self.water)

    def add_scour(self):
        print('Add scour:',self.scour)

    def start_wash(self):
        self.add_water()
        self.add_scour()
        print('Start wash...')

if __name__ == '__main__':
    # w = Washer()
    # w.start_wash()
    wb = Washer(100,10)
    wb.set_water(50)
    wb.set_scour(5)
    wb.start_wash()