# _*_ coding: utf-8 _*_
__author__ = 'wuhao'
__date__ = '2017/8/31 11:21'


class Medicine:
    name = ""
    price = 0.0

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def accept(self, visitor):
        pass


class Antibiotic(Medicine):
    def accept(self, visitor):
        visitor.visit(self)


class Coldrex(Medicine):
    def accept(self, visitor):
        visitor.visit(self)


# 药品类中有两个子类，抗生素和感冒药；

class Visitor:
    name = ""

    def setName(self, name):
        self.name = name

    def visit(self, medicine):
        pass


class Charger(Visitor):
    def visit(self, medicine):
        print "CHARGE: %s lists the Medicine %s. Price:%s " % (self.name, medicine.getName(), medicine.getPrice())


class Pharmacy(Visitor):
    def visit(self, medicine):
        print "PHARMACY:%s offers the Medicine %s. Price:%s" % (self.name, medicine.getName(), medicine.getPrice())


class ObjectStructure:
    pass


class Prescription(ObjectStructure):
    medicines = []

    def addMedicine(self, medicine):
        self.medicines.append(medicine)

    def rmvMedicine(self, medicine):
        self.medicines.append(medicine)

    def visit(self, visitor):
        for medc in self.medicines:
            medc.accept(visitor)
# python不支持静态分派
def max_num(x,y,z):
    return max(max(x,y),z)
def max_num(x,y):
    return max(x,y)

if __name__ == "__main__":
    yinqiao_pill = Coldrex("Yinqiao Pill", 2.0)
    penicillin = Antibiotic("Penicillin", 3.0)
    doctor_prsrp = Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)
    charger = Charger()
    charger.setName("Doctor Strange")
    pharmacy = Pharmacy()
    pharmacy.setName("Doctor Wei")
    doctor_prsrp.visit(charger)
    doctor_prsrp.visit(pharmacy)
