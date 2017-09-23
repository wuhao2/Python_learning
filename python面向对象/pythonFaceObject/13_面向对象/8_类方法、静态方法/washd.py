class Washer:
    company = "Le Xi"
    def __init__(self,water=10,scour=2):
        self._water = water
        self.scour = scour
        self.year = 2010

    @staticmethod
    def spins_ml(spins):
        # print("company:",Washer.company)
        # print('year:',self.year)
        return spins * 0.4

    @classmethod
    def get_washer(cls,water,scour):
        print("company:",Washer.company)
        print('year:',self.year)

        return cls(water,cls.spins_ml(scour))


    @property
    def water(self):
        return self._water

    @water.setter
    def water(self,water):
        if 0 < water <=500:
            self._water = water
        else:
            print("set Failure!")

    @property
    def total_year(self):
        return 2015 - self.year
    

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
    # print(Washer.spins_ml(8))
    # w = Washer()
    # print(w.spins_ml(8))
    # w = Washer(200,Washer.spins_ml(9))
    # w.start_wash()
    w = Washer.get_washer(100,9)
    w.start_wash()


