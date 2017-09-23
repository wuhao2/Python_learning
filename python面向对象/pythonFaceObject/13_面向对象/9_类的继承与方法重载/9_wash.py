class Washer:
    company = "Le Xi"
    def __init__(self,water=10,scour=2):
        self._water = water
        self.scour = scour

    @staticmethod
    def spins_ml(spins):
        return spins * 0.4

    @classmethod
    def get_washer(cls,water,scour):
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

class WasherDry(Washer):
    
    def dry(self):
        print('Dry clothes...')

    def start_wash(self):
        print("....")
        super().start_wash()
        print("....")

if __name__ == '__main__':
    w = WasherDry()
    w.start_wash()
    print(w.scour,w.company)
    w.dry()
